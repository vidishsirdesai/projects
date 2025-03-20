# An Example
As a loan approval manager at bank, I have gained valuable experience in approving, and rejecting loans for customers over the past 5 years. Through this experience, I have observed a pattern:

- Customers with a monthly income above 50k, and an age between 18 to 30 years, consistently have their loans approved.
- Customers earning below 30k a month, and having a credit score below 500 tend to default on their loans.

To streamline, and automate the loan approval process based on this information, write a pseudocode that can be used as an automatic machine for future approvals.

```python
if(income > 50k) and (age <= 18 and age <= 30): 
	set_flag = approve_loan
elif(income < 30k and credit_score < 500): 
	set_flag = reject_loan

if applicant_income > 50000:
	if 18 <= age <= 30:
		approve_loan
	else:
		reject_loan
elif income < 30000:
	if credit_score > 500:
		approve_loan
	else:
		reject_loan
```

What if there is a person who has not submitted the credit score? The above rule based logic will obviously fail. This approach is also called as hard coding.

And this led to the origins of ML. Computer scientists initially started using this approach to enable a computer to take a decision. (This is how ML originated).

But there were many problems with this approach. One for instance is that, this is unable to capture all the cases that could be encountered in real life. (only 3 cases are captured in the code: income, age and credit score).


# Motivation Behind Rule Based Modeling
Consider the following dataset,

| **Humidity** | **Play Golf** |
| --- | --- |
| High | No |
| High | No |
| High | No |
| Normal | Yes |
| Normal | Yes |

Predict if golf can be played, or not based on the humidity.

This data can be used to easily create a rule based model. Which looks like this,

```python
if humidity == "High":
	don't play golf
else:
	play golf
```

Now, if another parameter “outlook” is added,

| **Outlook** | **Humidity** | **Play Golf** |
| --- | --- | --- |
| Rainy | High | No |
| Rainy | High | No |
| Sunny | High | Yes |
| Sunny | Normal | Yes |
| Sunny | Normal | No |
| Rainy | High | No |
| Rainy | Normal | Yes |
| Sunny | Normal | Yes |
| Rainy | Normal | Yes |
| Sunny | High | No |

It would now become a little tricky to find a relationship between Outlook, Humidity and Play Golf, but with a little effort, it is not impossible.

```python
if outlook == "Rainy":
	if humidity == "High"
		play_golf = No
	else:
		play_goft = Yes
(following is the tricky part)
elif outlook == "Sunny"
```

Now, what if the data looked like this,

| **Outlook** | **Temperature** | **Humidity** | **Windy** | **Play Golf** |
| --- | --- | --- | --- | --- |
| Rainy | Hot | High | False | No |
| Rainy | Hot | High | True | No |
| Overcast | Hot | High | False | Yes |
| Sunny | Mild | High | False | Yes |
| Sunny | Cool | Normal | False | Yes |
| Sunny | Cool | Normal | True | No |
| Overcast | Cool | Normal | True | Yes |
| Rainy | Mild | High | False | No |
| Rainy | Cool | Normal | False | Yes |
| Sunny | Mild | Normal | False | Yes |
| Rainy | Mild | Normal | True | Yes |
| Overcast | Mild | High | True | Yes |
| Overcast | Hot | Normal | False | Yes |
| Sunny | Mild | High | True | No |

Finding a logic in this is even more difficult, and if even if you are able to figure one out, there is a very high chance that it might fail for a new data point.

Therefore, problems with rule based logic:

1. It is a complex, tedious process to formulate the rule as the data gets more, and more bigger in size (row-wise and column-wise).
2. Even if by slightest chance, a rule is formulated, there is a very high chance that it might fail if a new feature is introduced, or if the rule is not provided with inputs which are not coded in the logic.


# ML V. Classical Programming
Consider,

| **Input1** | **Input2** | **Output** |
| --- | --- | --- |
| 1 | 2 | 1.00 |
| 2 | 4 | 2.00 |
| 4 | 6 | 3.33 |
| 5 | 9 | 4.67 |
| 3 | 1 | 1.33 |
| 9 | 0 | 3.00 |
| 3 | 6 | 3.00 |
| 10  | 4  | ?? |

The relationship between input, an output is defined as,

$$
Output = \frac{Input_1 + Input_2}{3}
$$

Therefore for random Input1, and Input2,

| **Input1** | **Input2** | **Output** |
| --- | --- | --- |
| 10 | 4 | (10 + 4)/ 3 = 4.67 |

What you just did there was that, you performed a learning of sort.

Therefore, the pipeline can be summed up as,

- From the data → You found out how the inputs are related to the output → This relationship is used to predict the output for a new data point.

There is one problem, which is, for a human, when a limited data is shown, where the relationship was easy to find, it is easy to come up with a learning model.

But, what if the dataset were more complex and the relationship between the inputs and output was not so easy to find? for example,

| **age** | **sex** | **years_of_experience** | **salary** |
| --- | --- | --- | --- |
| . |  |  |  |
| . |  |  |  |
| . |  |  |  |
| 500 rows |  |  |  |

Salary is related to age, sex and years_of_experience as,
- $\text{Salary} = f\text{(age, sex, years-of-experience)}$

A mathematical algorithm is needed to find this above relation, that will help in finding this relationship.

Once the mathematical algorithm returns the relationship, it can be used to find/ predict the salary of a new employee.

When you enable a computer to find out the relationship between output, and various inputs that is when it can be said that the machine has learnt something.

There are various ML algorithms out there, each one specifically tuned to perform a particular type of task.

Learning these various ML algorithms is the objective henceforth (Which ML algorithm to use in what scenario and over what type of data?).


# Terminologies in ML
Consider,

| **age** | **sex** | **years_of_experience** | **salary** |
| --- | --- | --- | --- |
|  |  |  |  |
1. Data is the entire dataset, it is also called as set of examples/ input data/ historical data.
2. "salary" is known as the output column/ target column/ dependent feature/ y_label/ y.
How is the dependent variable chosen? This is chosen based on what we are interested in predicting (in this case, it is “salary”).
3. “age”, “sex” and “years_of_experience” are known as independent features/ predictors/ input variables/ input column/ x_labels/ x. x can be all numerical, all categorical, or they can be a combination of both. The x, are used to predict the y.


# Process of Machine Learning
1. Start with the historical data. This data comes with one dependent, and multiple features/ variable.
2. This historical data is fed to the ML algorithm (this is a mathematical machine). Once this is done, the machine will try to find out how x is related to y/ what is the relationship between inputs and output.
3. Once the relationship is found, it will return the formula which is called as the ML model.
ML model is the formula/ function that the ML algorithm has learnt. Which is given by y = f(x).
4. This formula can be used to make predictions.

ML Algorithm is the mathematical brain that can find out, how y is dependent on x.

ML model is the equation describing the y's dependency on the x (multiple).

The ML model is used in making the predictions on the new data.

In the process of ML, before the data (which comes with various x and a y) is fed to the ML algorithm, the data is split into train set, and test set. Generally, the train dataset will have 70% of the original data, and test dataset will have 30% of the original data. This is done randomly.

Note that, this is not the only splitting technique.

The train data is fed to the ML algorithm, the ML algorithm will use this as example to formulate the model.

$y = f(x_1, x_2)$

This model is then fed with the test data as input, and the model will predict the output. The predicted output is compared with the actual output to check the performance of the ML model.

Once the ML algorithm has generated some model, it is also important to check if this model is working or not. In order to achieve this, train-test split is done.

The above is the process of classical machine learning.


# What is Machine Learning?
Consider an example of a person who is going to attempt an examination, this person is given a reading material, which contained 70 questions from a total of 100 questions, along with the solution for each of the 70 questions, and 30 questions were given without solutions. This was done to check if this person has learnt the underlying concept, or not.

If the comparison made during the test is good then the ML model is said to be good.

Tom Mitchell of Carnegie Mellon described Machine Learning as, “*A computer program is said to learn from experience E with respect to some class of tasks T, and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.*”

Where,
- Task is the feature that the ML model is predicting.
- Experience is the historical data.
- Performance is the comparison between the actual outcome, and predicted outcome.


# Branches of Machine Learning
- Supervised Learning:
    - Supervised means the availability of/ presence of supervision. Meaning some kind of help is available to us.
    - Supervised ML algorithms work on the data that comes with both inputs, and output (independent, and dependent variables). Supervision here is the output variable (y_label).
    - These classes/ types of ML algorithms require the set of examples which come with the outcome, so that they can learn how the inputs are associated with output.
- Unsupervised Learning:
    - Unsupervised ML algorithms work on the data that comes with only input (independent variables)/ data with only features/ there is no target variable.
    - These algorithms help in finding out the association between various rows.
- Reinforcement Learning:
    - An agent is placed into an environment, and the agent learns by taking some actions, getting rewards, and losses etc.
- Semi-Supervised Learning:
    - Basically, you use unsupervised algorithms to create the labels, and supervised algorithms to train the model. Read about NER model and how it built.

### Supervised ML Algorithms are Further Classified as
- Regression
- Classification

These are two techniques which are dependent on the types of variables.

If the target variable of the data is continuous, then regression supervised algorithms are used.

If the target variable of the data is categorical, then classification supervised algorithms are used.

The input variables can be of continuous, or categorical.

The difference between classification, and regression is that, in classification we need the decision boundary to be far away from the data point on each side of it, and in regression we need the decision boundary to be close to all the data points.

### Unsupervised ML Algorithms are Further Classified as
- Clustering
- Association