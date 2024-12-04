# Manifolds

### What are manifolds?
Manifolds are formally defined as an intrinsically low dimensional structures in a high dimensional area.

Say that there is a 100 dimensional space, in here there is an object which has say 20 dimensions. This 100 dimensional space is called an ambient space (ambient space is a very high dimensional space). The 20 dimensional object is called a manifold.

Say that there are images of faces of people. Each image has say 24x24 dimensions. But most images can be represented by low dimensions as well. Say hair, lips, eyes are defined, then it is possible to distinguish between different faces. These defining parameters (hair, lips, and eyes) are called manifolds. Therefore, even though the image is high dimensional, it is possible to define it using these manifolds.

Multiple such manifolds make up a full object/ structure (here, face).

### How to find the manifolds?
One of the technique is to project the high dimensional data onto a low dimensional space. With this, most of the data/ the information present in the data is preserved for local data points.

### Manifold Hypothesis
It is an assumptions which says that, many of the real world datasets actually lie in a relatively low dimensional manifold.


# Curse of Dimensionality
The distance between the data points increases with increase in the number of dimensions.


# Scaling (Which One To Use?)
There are two types of scaling,
1. MinMax [0, 1]
2. Standard/ Normalization ((x - μ)/ σ)
3. There are also a few more scaling techniques. The above 2 are the most popular ones.
When the concept is not clear, both of them are tried.

Standardization centers the data around the mean. The most important bit is that, the distribution in preserved.

Consider,

| **Age (0 - 100)** | **Income (Varying)** |
| :-: | :-: |
|  |  |

If standard scaling is applied here, age will be centered around its mean and std dev, and income will be centered around its mean and std dev.

As a result, the distribution is preserved.

If min-max scaling is applied here, both the features will be scaled between 0 to 1.

As a result, the distribution is not preserved.

Standardization preserves the importance of each feature. Whereas, normalization brings the importance of all the features to the same level.

Consider the following image data,

| 0 | 83 | 255 | 99 |
| :-: | :-: | :-: | :-: |
| 95 | 77 | 17 | 90 |
| 88 | 100 | 45 | 79 |
| 45 | 0 | 0 | 99 |

Each number represents the intensity of each pixel.

If this data is to be fed to a neural network, standardization cannot be used in this case as there is no concept of distribution. Even if the distribution is preserved in the first layer of the NN, the distribution will change as it fed to the next layer.

Hence in image data, to ensure numerical stability, MinMax scaler is used. This also done to ensure the code to be safe in production.

# Notes
- Read about SLRM (Simple Linear Regression Model) and MLRM (Multiple Linear Regression Model).
Poly/ Ridge/ Lasso are heavily used in place of Linear Regression, because they give a little bit of flexibility.
All the features of Poly/ Ridge/ Lasso can be accessed in Simple Linear Regression Model.
- Baseline model is a simple model which will initiate the ground work, and at the same time is also interpretable.
But when in development, baseline model is something that can be pushed into production with a little bit of caution.
Baseline is something that is ready to be merged into the main branch, but at the same time, it can be bettered using optional tools.
Say a baseline model is built with desired accuracy, but is not immediately deployed into production, instead a wait time is given to see if it can be bettered before deployment.