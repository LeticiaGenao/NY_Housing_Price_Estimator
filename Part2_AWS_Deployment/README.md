### Part2_AWS_Deployment

**Overview**
This directory outlines the process and setup used for the AWS components of the New York Housing Price Estimator project. Although full deployment through AWS SageMaker was not achieved, significant groundwork was laid, including the setup of an Amazon Elastic Container Registry (ECR) and utilization of Amazon S3 for storage. This section of the project is ongoing, and the documentation here reflects the current state of the AWS deployment process.

**Contents**
- `requirements.txt`: List of Python dependencies required for running the application.
- `Dockerfile`: The Dockerfile used in Part1_Local_and_Heroku_Deployment is also appropriate for deployment on AWS via Amazon Elastic Container Registry (ECR) and Amazon SageMaker.
- `images/`: Contains screenshots demonstrating the setup of AWS resources, including:
  - ECR repository setup (ecr_image.PNG)
  - SageMaker Jupyter notebook instance (jupyter_notebook_instance.PNG)
  - S3 bucket overview and data organization (s3_bucket.PNG, s3_bucket_data.PNG, s3_bucket_model.PNG, s3_bucket_predictions.png)****

**Usage**
1. S3 Bucket Configuration:
   - The screenshots under images/ illustrate the S3 bucket setup which hosts model files, datasets, and prediction results. The actual S3 bucket is managed directly in AWS.
2. SageMaker Usage:
   - Development and testing are conducted through a SageMaker notebook instance, with evidence provided in screenshot form.
3. Ongoing Development:
   - Updates and attempts at full deployment will continue as part of the project’s lifecycle. Further documentation will be added as the deployment progresses.
