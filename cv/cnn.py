import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from scipy import signal

# defining the base Layer class
class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def forward(self, input):
        # return output
        pass

    def backward(self, output_gradient, learning_rate):
        # update parameters and return input gradient
        pass


# the convolution operation is performed using correlate2d() method of scipy package
class Convolutional(Layer):

    def __init__(self, input_shape, kernel_size, depth):
        # input_shape is 3 dimensional (d x h x w), 
        # input_depth = number of image input channels, input_height = image height and input_width = image width
        input_depth, input_height, input_width = input_shape

        self.input_shape = input_shape

        # depth = number of kernels in the convolutional layer
        self.depth = depth
        
        # number of channels in the image are 3 for a RGB image and 2 for a grayscale image
        self.input_depth = input_depth

        # calculating the convolutional layer output of 3 dimensions
        self.output_shape = (depth, input_height - kernel_size + 1, input_width - kernel_size + 1)

        # kernel_shape specifies the shape of the Kernel produced
        # it has 4 dimensions, depth = number of Kernels (depth), input_shape = image channels, kernel_size = kernel dimension
        self.kernels_shape = (depth, input_depth, kernel_size, kernel_size)

        # randomly initializing the Kernel weights
        self.kernels = np.random.randn(*self.kernels_shape)

        # randomly initializing the biases
        self.biases = np.random.rand(*self.output_shape)

    # forward pass takes input and computes the output by applying the above convolution
    def forward(self, input):
        self.input = input

        # initialize the output matix with output_shape
        self.output = np.zeros(self.output_shape)

        # 2 nested for loops, first one to traverse all the Filters (depth), second one to traverse all the channels (input_depth) in every input image
        for i in range(self.depth):
            for j in range(self.input_depth):

                # output is calculated by adding the biases of the layer with the cross correlation between image and the Kernel, "valid" stands for no padding.
                self.output[i] += self.biases[i] + signal.correlate2d(self.input[j], self.kernels[i, j], "valid")

        return self.output
    
    def backward(self, output_gradient, learning_rate):
        # initialize the gradient of the Kernels as 0
        kernel_gradient = np.zeros(self.kernels_shape)
        # initialize the gradient of the inputs as 0
        input_gradient = np.zeros(self.input_shape)

        # the following nested for loops update the gradients
        # first all the Filters (depth) are traversed
        # then all the channels in every input image (input_depth) are traversed
        # this is done to update the gradients of Kernels and inputs
        for i in range(self.depth):
            for j in range(self.input_depth):

                # the following code line calculates Kernel gradient in every i and j index in the Kernel by computing the correlation between image and output gradient
                kernel_gradient[i, j] = signal.correlate2d(self.input[j], output_gradient[i], "valid")
                # the following code line calculates input gradient by sliding the Kernel on the output gradient matrix
                input_gradient[j] += signal.convolve2d(output_gradient[i], self.kernels[i, j], "full")

        # update the Kernels and biases with respect to learned features (stored in gradients)
        # gradients are multiplied with the learning rate to update the Kernels and biases
        self.kernels -= learning_rate * kernel_gradient
        self.biases -= learning_rate * np.sum(output_gradient)

        return input_gradient
    

# base Activation class to specify the default properties of the Activation layer from which all the activation functions are derived
class Activation(Layer):
    
    def __init__(self, activation, activation_prime):

        # calculation for the activation function
        self.activation = activation
        # calculation for derivative of the activation function which will be handy while backpropagation
        self.activation_prime = activation_prime

    def forward(self, input):
        self.input = input
        return self.activation(self.input)
    
    def backward(self, output_gradient, learning_rate):
        # multiplying the output gradient and the derivative of the loss to impleent the backward function for the activation
        return np.multiply(output_gradient, self.activation_prime(self.input))
    

class ReLU(Activation):
    def __init__(self):
        def relu(x):
            return np.where(x > 0, x, 0)
        
        def relu_prime(x):
            return np.where(x <= 0, 0, 1)
        
        super().__init__(relu, relu_prime)


class TanH(Activation):
    def __init__(self):
        def tanh(x):
            return np.tanh(x)
        
        def tanh_prime(x):
            return 1 - np.tanh(x) ** 2
        
        super().__init__(tanh, tanh_prime)


class Softmax(Layer):
    def forward(self, input):
        tmp = np.exp(input)
        self.output = tmp/ np.sum(tmp)
        return self.output
    
    def backward(self, output_gradient, learning_rate):
        n = np.size(self.output)
        return np.dot((np.identity(n) - self.output.T) * self.output, output_gradient)
    

class MaxPool(Layer):
    def __init__(self, input_shape, kernel_size, depth, stride):
        # input_shape is 3 dimensional (d x h x w), input_depth = number of image input channels, input_height = image height, input_width = image width
        input_depth, input_height, input_width = input_shape
        # specify the shape of the input
        self.input_shape = input_shape
        # specify the Kernel size of the MaxPool operation
        self.kernel_size = kernel_size
        self.kernel_shape = (depth, input_depth, kernel_size, kernel_size)
        # specify the depth or number of Filters
        self.depth = depth
        # specify the depth or channels of the input
        self.input_depth = input_depth
        # initializing the kernel with random values of shape (kernel_shape)
        self.kernel = np.random.randn(*self.kernel_shape)
        self.stride = stride
        self.input_height, self.input_width = input_height, input_width

    def forward(self, input):
        self.input = input

        KH = 1 + (self.input_height - self.kernel_size)// self.stride
        KW = 1 + (self.input_width - self.kernel_size)// self.stride
        self.output = np.zeros((self.input_depth, KH, KW))

        for depth in range(self.input_depth):
            for r in range(0, self.input_height - 1, self.stride):
                for c in range(0, self.input_width - 1, self.stride):
                    self.output[depth, r// self.stride, c// self.stride] = np.max(self.input[depth, r: r + self.kernel_size, c: c + self.kernel_size])
        
        return self.output
    
    def backward(self, output_gradient, learning_rate):
        self.output_gradient = np.zeros(self.input_shape)
        # initialize gradient of the layer
        dx = np.zeros(self.input_shape)
        
        # the first for loop is to traverse through all the filters (depth)
        # the second for loop is to traverse through the height of the image
        # the third for loop is to traverse through the width of the image
        for depth in range(self.input_depth):
            for r in range(0, self.input_height - 1, self.stride):
                for c in range(0, self.input_width - 1, self.stride):
                    grad_pool = self.output[depth, r * self.stride: r * self.stride + self.kernel_size, c * self.stride: c * self.stride + self.kernel_size]
                    mask = (grad_pool == np.max(grad_pool))
                    dx[depth, r * self.stride: r * self.stride + self.kernel_size, c * self.stride : c * self.stride + self.kernel_size] = mask * self.output_gradient[depth, r, c]

        return dx
    

class Reshape(Layer):
    def __init__(self, input_shape, output_shape):
        # specifying the shape of input and output in the constructor
        self.input_shape = input_shape
        self.output_shape = output_shape

    def forward(self, input):
        # forward reshapes the input to the shape of output
        return np.reshape(input, self.output_shape)
    
    def backward(self, output_gradient, learning_rate):
        # backward reshapes the output to the shape of input
        return np.reshape(output_gradient, self.input_shape)
    

class Dense(Layer):
    def __init__(self, input_size, output_size):
        # defining the weights matrix shape
        self.weights = np.random.randn(output_size, input_size)
        # defining the m=bias matrix shape
        self.bias = np.random.randn(output_size, 1)

    def forward(self, input):
        self.input = input
        # implementing z = w.x + b
        return np.dot(self.weights, self.input) + self.bias
    
    def backward(self, output_gradient, learning_rate):
        # calculate weight gradient by dot product of output gradient and transpose of input
        weight_gradient = np.dot(output_gradient, self.input.T)
        # calculatw the input gradient by performing dot product of weights transpose and output gradient
        input_gradient = np.dot(self.weights.T, output_gradient)
        # update the weights of the layer with weight gradient with respect to the learning rate
        self.weights -= learning_rate * weight_gradient
        # update the bias of the layer with output gradient with respect to the learning rate
        self.bias -= learning_rate * output_gradient

        return input_gradient
    

def log_loss(y_true, y_pred):
    return np.mean(- y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred))

def log_loss_prime(y_true, y_pred):
    #log_loss_prime works the same way as log loss
    # but is the derivative of the above function which will be used to
    # compute layers gradients durin back propagation
    return ((1 - y_true)/ (1 - y_pred) - y_true/ y_pred) / np.size(y_true)


def train(network, loss, loss_prime, x_train, y_train, epochs = 10, learning_rate = 0.01):
    for e in range(epochs):
        error = 0
        idx = 0
        for x, y in zip(x_train, y_train):
            # print the progress
            if (idx + 1) % 100 == 0:
                print(f"Epoch {e}: {idx + 1}/ {len(y_train)}")

            idx += 1

            # forward pass to predict on the training data
            output = predict(network, x)

            # summing the losses to optimize the network's weights and biases
            error += loss(y, output)

            # performing backward pass through every layer by computing the gradients
            grad = loss_prime(y, output)
            for layer in reversed(network):
                grad = layer.backward(grad, learning_rate)

        error /= len(x_train)
        print(f"Epoch: {e + 1}/ {epochs}, loss = {error}")

# defining a method to predict using the NN
def predict(network, input):
    output = input
    
    # performing a forward pass to the network
    for layer in network:
        output = layer.forward(output)

    return output

