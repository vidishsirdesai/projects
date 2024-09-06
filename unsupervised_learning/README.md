# Introduction
Unsupervised learning models are applied on data that only has features and no label/ target variable. For example,

| age | income | total_purchase_value | number of orders |
| :-: | :----: | :------------------: | :--------------: |


The task of an unsupervised learning algorithm is not to make a prediction, but to find a relationship or similarity between rows or a cluster of rows.

# The Basic ML Setup

### Model Training
The features are fed as input to an algorithm, the algorithm learns the equation that maps the inputs to the output. Once the algorithm learns the mapping equation, the model is said to be trained.
```mermaid
  graph TD;
      Features and Target --> Algorithm --> Model;
```