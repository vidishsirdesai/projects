# What is AWS SageMaker?
AWS SageMaker is a cloud-based machine learning platform that allows developers to build, train, and deploy ML models at scale. It provides a comprehensive set of tools and services that simplify the process of developing and deploying ML models, making it accessible to a wider range of users.

### Key features
- Fully managed service: SageMaker handles the underlying infrastructure, allowing developers to focus on building their models.
- Scalability: It can scale to handle large datasets and workloads.
- Integration with other AWS services: SageMaker integrates seamlessly with other AWS services, such as S3 for data storage and EC2 for compute resources.
- Pre-built algorithms and frameworks: SageMaker offers a variety of pre-built algorithms and frameworks, making it easier to get started with machine learning.
- Notebook instances: SageMaker provides Jupyter notebooks for data exploration, analysis, and model development.
- Hyperparameter tuning: It helps optimize model performance by automatically tuning hyperparameters.
- Model deployment: SageMaker makes it easy to deploy models into production and manage their lifecycle.

### Why is AWS SageMaker important?
SageMaker is important because it makes machine learning more accessible, efficient, scalable, and cost-effective, enabling businesses to develop and deploy AI applications more rapidly.

SageMaker has 2 variations,
1. SageMaker Studio
2. SageMaker Notebook

Both are used for building and deploying ML models. The following is a comparison of the both,

### SageMaker studio
- Integrated development environment (IDE): SageMaker Studio provides a comprehensive IDE tailored for machine learning.
- Multiple notebooks: Multiple notebooks can be created and can be managed within a single project.
- Version control: Studio integrates with GitHub and other version control systems for collaborative development.
- Experiment tracking: It helps track experiments, compare results, and reproduce models.
- TensorBoard integration: Visualize training metrics and model graphs directly within Studio.
- Customization: The IDE can be customized to suit the user's preferences.

### SageMaker notebook
- Jupyter notebook: A popular open-source tool for data analysis and visualization.
- Single notebook: Each notebook is a standalone document.
- Basic version control: Version control for notebooks can be manually managed.
- Limited experiment tracking: Although experiments can be tracked manually, it's not as integrated as Studio.
- TensorBoard integration: Requires manual configuration to use TensorBoard with SageMaker Notebook.
- Less customization: Compared to Studio, SageMaker Notebook offers fewer customization options.

### When to choose SageMaker studio?
- Collaborative projects: Choose studio while working with a team and features like version control and experiment tracking are needed.
- Complex models: For building and managing complex machine learning models.
- Customization: Choose studio if a highly customizable IDE is preferred.

### When to choose SageMaker notebook?
- Simple projects: For small-scale or personal projects.
- Familiarity with Jupyter Notebook: If you're already comfortable with Jupyter Notebook and don't need advanced features.
- Cost-effectiveness: SageMaker Notebook might be more cost-effective for basic use cases.


# What is S3?



# What is `boto3`?
`boto3` is an AWS SDK for Python. It provides an interface to interact with AWS services like S2, EC2, DynamoDB, Lambda, etc,. Using `boto3`, Python code to manage and control AWS resources can be programmatically written.


# Problem Statement
Given a bank marketing dataset, the goal is to predict if a person is going to make a fixed/ term deposit.


# Excercise
1. Login to the AWS account.
2. Once logged in, make sure to select the region, for the sake of this excercise, the region is set to "us-east-1".
3. Search for SageMaker in the search bar, and open it in a new tab.
4. Under "Applications and IDEs", click on "Notebooks", then click on "Create notebook instance".
5. Enter a name for the notebook (e.g. `bank-marketing`), under "Notebook instance name".
6. Select "Note instance type" and "Platform identifier". For the sake of this excercise, they are set to "ml.t3.medium" and "Amazon Linux 2, Jupyter Lab 3".
7. Under "Permissions and encryption" > "IAM role", select "Create a new role". Then check "Any S3 bucket" under "S3 buckets you specify".
8. Click on "Create role".
9. Now click on "Create notebook instance", and wait for the notebook instance to get created. Once created, the status should reflect "InService".
10. Once the notebook is ready, click on "Open Jupyter" under "Actions".
11. A Jupyter Notebook homepage should be opened in a new tab in the browser.
12. Select "New" and then select "conda_python3".
13. A new Jupyter Notebook should be opened with the name `Untitled`.
14. Change the name to `bank_marketing`.
15. Import the required modules into the notebook. Code,
```Python
import sagemaker
import boto3
from sagemaker.amazon.amazon_estimator import get_image_uri 
#alternative
from sagemaker.amazon.amazon_estimator import image_uris
from sagemaker.session import s3_input, Session
```
16. Assign a name to the S3 bucket, and then extract and store the region that was selected in a variable. Code,
```Python
# name the s3 bucket
bucket_name = "bank-app-mlops"
# mention the bucket name
my_region = boto3.session.Session().region_name
my_region
```
17. Create an S3 bucket to save the data in the bucket. The reason for doing this is that the data in Jupyter Notebook is not going to persist after the session is closed. Code,
```Python
# create a bucket
# create a bucket
s3 = boto3.resource("s3")
try:
    if my_region == "us-east-1":
        s3.create_bucket(Bucket = bucket_name)
    print("s3 bucket created successfully")
except Exception as e:
    print("s3 error: ", e)
```
18. Go to the tab which has the AWS homepage open, and search for "S3", and open it in a new tab.
19. A new bucket should have been created successfully.
20. To save the data inside the bucket, a folder structure has to be created inside the s3 bucket. Code,
```Python
# set an output path where the trained model will be saved
prefix = "xgboost-as-a-built-in-algo"
output_path = "s3://{}/{}/output".format(bucket_name, prefix)
output_path
```
21. To download and save the data,
```Python
import pandas as pd
import urllib

try:
    #the bank data is in one hot encoded format already
    urllib.request.urlretrieve ("https://d1.awsstatic.com/tmt/build-train-deploy-machine-learning-model-sagemaker/bank_clean.27f01fbbdf43271788427f3682996ae29ceca05d.csv", "bank_clean.csv")
    print("Success: Downloaded bank_clean.csv.")
except Exception as e:
    print("Data load error: ", e)

try:
    model_data = pd.read_csv("./bank_clean.csv", index_col = 0)
    print("Success: Data loaded into dataframe.")
except Exception as e:
    print("Data load error: ", e)
```
22. Split the data into train set and test set. Code,
```Python
import numpy as np
train_data, test_data = np.split(model_data.sample(frac = 1, random_state = 1729), [int(0.7 * len(model_data))])
print(train_data.shape, test_data.shape)
```
23. Save the train dataset, and test dataset into the bucket. Code,
```Python
import os

# formatting the train data
pd.concat(
    [train_data["y_yes"], train_data.drop(["y_no", "y_yes"], axis = 1)],
    axis = 1
).to_csv("train.csv", index = False, header = False)

# uploading train.csv in the bucket
boto3.Session().resource("s3").Bucket(bucket_name).Object(os.path.join(prefix, "train/train.csv")).upload_file("train.csv")

# now storing the training csv into a variable 
s3_input_train = sagemaker.TrainingInput(s3_data = "s3://{}/{}/train".format(bucket_name, prefix), content_type = "csv")

# formatting the test data
pd.concat(
    [test_data["y_yes"], test_data.drop(["y_no", "y_yes"], axis = 1)], 
    axis = 1
).to_csv("test.csv", index = False, header = False)

# uploading test.csv in the bucket
boto3.Session().resource("s3").Bucket(bucket_name).Object(os.path.join(prefix, "test/test.csv")).upload_file("test.csv")

s3_input_test = sagemaker.TrainingInput(s3_data = "s3://{}/{}/test".format(bucket_name, prefix), content_type = "csv")
```
24. Train the XGBoost model. Code,
```Python
# this line automatically looks for the XGBoost image URI and builds an XGBoost container.
# specify the repo_version depending on your preference.
container = image_uris.retrieve("xgboost", boto3.Session().region_name, "1.5-1")
```
25. Define the hyperparameters. Code,
```Python
# initialize hyperparameters
hyperparameters = {
    "max_depth": "5",
    "eta": "0.2",
    "gamma": "4",
    "min_child_weight": "6",
    "subsample": "0.7",
    "objective": "binary:logistic",
    "num_round": 50
}
```
26. Construct a SageMaker estimator that calls the xgboost-container. Code,
```Python
estimator = sagemaker.estimator.Estimator(
    image_uri = container, 
    hyperparameters = hyperparameters,
    role = sagemaker.get_execution_role(),
    instance_count = 1, 
    instance_type = "ml.m5.2xlarge",
    volume_size = 5, # 5 GB
    output_path = output_path
)
```
27.  Train the model. Code,
```Python
estimator.fit({"train": s3_input_train, "validation": s3_input_test})
```
28. To deploy, a serializer is needed. Therefore, a serializer has to be created. Code,
```Python
from sagemaker.serializers import CSVSerializer
xgb_predictor = estimator.deploy(initial_instance_count = 1, instance_type = "ml.m4.xlarge", serializer = CSVSerializer())
```
29. Model deployment is now complete. Before predicting on a new data point deserialization has to be done. Code,
```Python
# load the data into an array
test_data_array = test_data.drop(["y_no", "y_yes"], axis = 1).values
print(test_data_array.shape)

#xgb_predictor.content_type = 'text/csv' # set the data type for an inference
#xgb_predictor.serializer = CSVSerializer() # set the serializer type

# predict
predictions = xgb_predictor.predict(test_data_array).decode("utf-8")
print(predictions)
```
30. Store the predictions into an array. Code,
```Python
# convert the prediction into an array
predictions_array = np.fromstring(predictions[1:], sep = "\n")
print(predictions_array.shape)
```
31. Compute the model metrics. Code,
```Python
import sklearn.metrics

cutoff = 0.5
print(sklearn.metrics.confusion_matrix(test_data["y_yes"], np.round(predictions_array)))
print(sklearn.metrics.classification_report(test_data["y_yes"], np.round(predictions_array)))
```
32. The goal of creating an endpoint however, is to access it from a device that is on a different network. To do so, check the endpoint name. Code,
```Python
xgb_predictor.endpoint_name
```
33. The above endpoint name should match with the one on the S3 tab (AWS S3 > Buckets > bank-app-mlops > xgboost-as-abuilt-in-algo/ > output/).
34. After this check has been made, install boto3 on the local using the command, `pip install boto3`.
35. Create a notebook locally with the name, `experiment.ipynb`. Import the necessary modules,
```Python
import boto3
import json
```
36. Goto the tab with the AWS homepage, and search for "IAM", and open "IAM" in a new tab.
37. Once inside IAM > Users, click on the existing "User name". Then click on "Security credentials".
38. Scroll down to "Access keys" section, and click on "Create access key". Then select "Command Line Interface (CLI)". Once the selection is made, check the box under "Confirmation", and click on "Next".
39. Enter a Description tag value in the next screen (e.g., MY_ACCESS_TOKEN), and click on "Create access key". Make sure to NOT close the tab that has the access key details displayed (either this, or click on "Download .csv file").
40. Copy the "Access key" and "Secret access key" and assign it to its respective variable in `experiment.ipynb`.
```Python
access_id = "**********"
access_key = "**********"

test = "29, 2, 999, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0"

runtime = boto3.Session().client(
    "sagemaker-runtime",
    region_name = "us-east-1",
    aws_access_key_id = access_id,
    aws_secret_access_key = access_key
)
```
41. Also copy the endpoint name from the notebook in SageMake and assign it to its respective variable in `experiment.ipynb`. Code,
```Python
response = runtime.invoke_endpoint(
    EndpointName = "**********",
    ContentType = "text/csv",
    Body = test
)
```
42. The class probability can now be predicted. Code,
```Python
result = response["Body"].read().decode("ascii")
print("Predicted Class Probabilities: {}.".format(result))
```
43. It is also possible to connect with S3 and find out the available buckets. Code,
```Python
#name of the buckets in your account
s3 = boto3.client(
    "s3",
    region_name = "us-east-1",
    aws_access_key_id = access_id,
    aws_secret_access_key = access_key
)

response = s3.list_buckets()

# Output the bucket names
print("Existing buckets: ")
for bucket in response["Buckets"]:
    print(f"{bucket['Name']}")
```