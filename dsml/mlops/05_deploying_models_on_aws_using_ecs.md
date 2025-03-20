# What Is AWS?
AWS is a cloud service by Amazon. 


# What Are Cloud Services?
Cloud services are computing resources that are delivered over the internet, on demand, and accessed through a pay-as-you-go pricing model. Instead of owning and maintaining physical hardware, businesses can access these resources from a cloud provider, such as AWS, Microsoft Azure, or Google Cloud Platform.

### Types of Cloud Services
- Infrastructure as a Service (IaaS): Provides fundamental computing resources like servers, storage, and networking.
- Platform as a Service (PaaS): Offers a platform for developing, testing and deploying applications.
- Software as a Service (SaaS): Delivers applications over the internet, allowing users to access them without needing to install or maintain software on their own devices.

### Examples of Cloud Services
- Cloud storage: Amazon S3, Google Cloud Storage, Microsoft Azure Blob Storage.
- Compute services: Amazon EC2, Google Compute Engine, Microsoft Azure Virtual Machines.
- Database services: Amazon RDS, Google Cloud SQL, Microsoft Azure SQL Database.
- Analytics services: Amazon Redshift, Google BigQuery, Microsoft Azure Synapse Analytics.

### Why are Cloud Services necessary?
The training of ML models, especially Deep Learning, models requires a lot of computing resources (like GPUs). Consider that in a worst case scenario, the model has to be trained on a 100GB GPU. This would require you to have the resources necessary locally present on site in order to complete this task. This would also require that these resources are serviced and maintained at regular intervals. This obviously is not a very friendly in financial terms, in case of small-tier, or even a mid-tier organization.

This is why cloud services are important. They take away this burden from such organizations and offer them these resources, as explained, on a pay-as-you-go or pay-as-you-use pricing model. Meaning, if 100GB of GPU space is used for 2 hours, then the organization using it is only charged for that much resource for that much amout of time.

### How to use these services?
An access is required in order to use these services. For the sake of this excercise, An AWS account is created and access for a lab is purchased for the same.


# Agenda Of This Excercise
The agenda of the excercise is to deploy the project in container on the cloud using Amazon Elastic Container Service (ECS).


# What Is Amazon ECS?
Amazon ECS is a fully managed container orchestration service that helps in deploying, managing and scaling containerized applications. It is designed to simply the process of running containers on AWS.

### Key features
- Container orchestration: ECS manages the lifecycle of containers, including scheduling, scaling and load balancing.
- Integration with AWS services: ECS integrates seamlessly with other AWS services like Amazon Elastic Compute Cloud (EC2), Amazon Elastic Container Registry (ECR), and Amazon S3.
- Scalability: ECS helps in scaling the applications up or down based on demand.
- High availability: ECS provides built-in fault tolerance and high availability to ensure that the applications remain running.
- Security: ECS offers robust security features, such as network isolation and IAM integration.


# What Is Amazon ECR?
Amazon ECR is a fully managed container registry service that helps in storing and managing Docker images. It provides a secure and scalable way to store the container images, making them easily accessible for deployment to various environments.

### Key Features
- Secure storage: ECR encrypts the images at rest and in transit, ensuring that they are protected from unauthorized access.
- Scalability: ECR can handle large numbers of images and can scale automatically to meet the needs.
- Integration with ECS: ECR integrates seamlessly with ECS, making it easy to deploy the container images to ECS clusters.
- Image scanning: ECR can scan the images for vulnerabilities and provide remedation recommendations.
- Private repositories: Private repositories can be created to store the images securely.


# How Is ECS Different To ECR?
### ECS
- Primary function: Orchestrates and manages containerized applications.
- Role: Handles the deployment, scaling, and lifecycle management of containers.
- Functionality: Provides features like task definition, service creation, load balancing, and integration with other AWS services.

### ECR
- Primary function: Stores and manages Docker and OCI (Open Container Initiative) images.
- Role: Think of it as a repository for the container images.
- Functionality: Provides secure storage, versioning, and scanning for vulnerabilities.

In a nutshell, ECR is where the container images are stored, and ECS is the platform that runs and manages those images.


# What Is Container Orchestration?
Container orchestration is the process of automating the management of containerized applications. It involves tasks such as,
- Scheduling: Assigning containers to a specific hosts or nodes in a cluster.
- Scaling: Automatically scaling the number of containers up or down based on demand.
- Load balancing: Distributing traffic across multiple containers to improve performance and reliability.
- Health checks: Monitoring the health of the containers and restarting failed containers.
- Networking: Managing the network connectivity between containers and external services.

### Popular container orchestration platforms
- Kubernetes: An open-source platform widely used for managing containerized applications.
- Docker Swarm: A built-in orchestration tool for Docker.
- Amazon ECS: A managed container orchestration service from AWS.
- Google Kubernetes Engine (GKE): A managed Kubernetes service from Google Cloud Platform.


# What Is AWS Fargate?
Amazon ECS with Fargate is a serverless compute engine for containers. It helps to run containers without having to provision or manage servers. This means, focus can be on building applications rather than worrying about the underlying infrastructure.

### How Fargate works?
1. A task definition is defined that specifies the container image and its configuration.
2. A service is created that runs the task definition.
3. Fargate automatically provisions and manages the necessary infrastructure to run the containers.


# What Is Amazon E2C?
Amazon Elastic Compute Cloud (EC2) is a web service that provides on-demand compute capacity in the cloud. It allows to rent virtual computers (instances) with various configurations (CPU, memory, storage) to run the applications.

### Key features
- On-demand instances: Instances can be launched whenever they are needed and are paid for only the time for which they were running for.
- Variety of instance types: EC2 offers a wide range of instance types to suit different workloads, from general-purpose to high-performance computing.
- Scalability: EC2 instances can be easily scaled up or down to meet changing demands.
- Flexibility: EC2 supports various operating systems and software applications.
- Integration with other AWS services: EC2 integrates seamlessly with other AWS services like S3, RDS, and EFS.


# Excercise
1. Login to the AWS account.
2. Make sure to select the region, for the sake of this excercise, the region is set to "us-east-1".
3. Download the aws cli. Link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html.
4. Once the website (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) gets loaded, goto macOS > Command line installer - All users, and copy the command, `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"`.
5. Then run, `sudo installer -pkg ./AWSCLIV2.pkg -target /`.
6. The aws cli helps to authenticate the local machine to the AWS system. This is similar to running the `git config` newly.
7. To confirm the installation, run, `which aws`. The `which` command helps to find the location of the executables.
8. On the AWS account website, search for "IAM". IAM is where access for all the AWS accounts is managed from. Meaning, access to certain parts of AWS can be granted or revoked.
9. Once inside the IAM Dashboard, click on Users.
10. Once inside IAM > Users, click on the existing "User name". Then click on "Security credentials".
11. Scroll down to "Access keys" section, and click on "Create access key". Then select "Command Line Interface (CLI)". Once the selection is made, check the box under "Confirmation", and click on "Next".
12. Enter a Description tag value in the next screen (e.g., MY_ACCESS_TOKEN), and click on "Create access key". Make sure to NOT close the tab that has the access key details displayed (either this, or click on "Download .csv file").
13. Open the terminal window and run, `aws configure`.
14. Enter the AWS Access Key ID. This displayed on the "Retrive access keys" page.
15. Then enter the AWS Secret Access Key. This is also displayed on the "Retrive access keys" page.
16. Enter the Default region name. (`us-east-1`).
17. Enter the Default output format as `json`.
18. The local machine is now setup to interact with AWS using the AWS CLI.
19. Click "Done" on the "Retrieve access keys" page.
20. Now search for "ECR" in the "Console Home", and open "ECR" in a new tab.
21. Goto the project directory in the terminal, and build the docker image using the command, `docker build --platform=linux/amd64 --tag=admission_prediction .`.
22. Once the image is built, it has to be pushed to the AWS ecosystem. To do that, goto ECR, and click on "Create" under "Create a repository".
23. Enter a name for the repo, `admission_prediction`, and click "Create".
24. Once inside "Private repositories" page, click on the "admission_prediction". Then click on "View push commands".
25. The first command, `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 628837189499.dkr.ecr.us-east-1.amazonaws.com`, helps in logging into the AWS ecosystem.
26. There is no need to build the docker image again.
27. Tag the image so that the image can be pushed to this repo using the command, `docker tag admission_prediction:latest 628837189499.dkr.ecr.us-east-1.amazonaws.com/admission_prediction:latest`
28. Goto the Docker Desktop app, under images it can be seen that another image is created.
29. Push the Docker image to the the AWS repo using the command, `docker push 628837189499.dkr.ecr.us-east-1.amazonaws.com/admission_prediction:latest`.
30. Now click on "Close" on the "Push commands for admission_prediction" pop up, and wait for the image to be pushed to the AWS repo.
31. Goto Console Home tab in the browser, and search for "ECS", and open it in a new tab.
32. Click on "Create cluster". In the next page, name the cluster (e.g., `admission_prediction_cluster`).
33. Under "Infrastructure", select "AWS Fargate", and click on "Create".
34. Click on the cluster name that was created, then click on "Task definitions".
35. Under "Task definition", click on "Create new task definition".
36. Enter a name under "Task definition family" (e.g., `admission_prediction_task`).
37. Under "Infrastructure requirements", set "Operationg system/Architecture" to "Linux/X86_64". 
38. Under "Container - 1", Name the container (e.g., `admission_prediction_container`).
39. Goto the ECR tab on the browser, and copy "Copy URI". Now, go back the the Task definition tab, and paste the "Image URI" which was copied.
40. Once done, click on "Create" at the bottom of the page. The task, i.e., the container service, should get created successfully.
41. Click on "Deploy", and select "Run task".
42. In the next page that opens, goto "Networking", and check "Create a new security group".
43. Under "Type", choose "HTTP". 
44. Under "Source", choose "Anywhere".
45. Next, click on "Add rule".
46. Under "Type", choose "Customised TCP" and set "Port range" to 5000.
47. Under "Source", choose "Anywhere".
48. Click on "Create" at the bottom of the browser page.
49. On the next page, scroll down to the bottom of the page, and under "Tasks", click on the refresh option.
50. Check if the "Last status" shows as "Running".
51. Once the status displays as "Running", click on the task under "Tasks", scroll down to "Configuration", and look for "Public IP", click on "open address".
52. On the search bar of the browser, add, `http://<IP>:5000` to launch the page.
53. Open the Postman application, and send a POST request to `http://<IP>:5000/predict`.
54. Pass the parameters in the dictionary format, `{"gre_score": 300, "toefl_score": 100, "university_rating": 4, "sop": 3, "lor": 4, "cgpa": 8.90, "research": "Yes"}`.
55. Click on send to get the response.
56. The application is now up and running on the cloud.
57. This HTTP link can be shared and can be accessed by anyone now.


# How To Stop The Services?
1. On ECS, goto Clusters > Tasks > Configuration, and then select "Stop".
2. Then goto Clusters, click on "Delete cluster". Type, `delete <name_of_the_cluster>`, click on "Delete".
3. Goto Amazon ECR > Private Registry > Repositories, select the image and click on "Delete".
4. Type, `delete` and click on "Delete".
5. Goto Amazon ECR > Private Registry, select the repository and click on "Delete".
6. Finally goto the cloudlabs tab, and click on "Stop". This will stop the session.