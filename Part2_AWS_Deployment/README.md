### Part2_AWS_Deployment

**Overview**
This directory contains the Dockerfile and deployment instructions for deploying the model on AWS SageMaker using Docker containers. It provides a Dockerized version of the model, enabling easy deployment and scalability.

**Contents**
- `Dockerfile`: Instructions for building a Docker image containing the model and its dependencies.
- `requirements.txt`: List of Python dependencies required for running the application.
- `deploy.sh`: Shell script for deploying the Docker image on AWS SageMaker.
- `build_and_push.sh`: Shell script for building the Docker image and pushing it to Amazon ECR (Elastic Container Registry).

**Usage**
1. Build the Docker image by running:
   - sh build_and_push.sh
2. Deploy the Docker image on AWS SageMaker by executing:
   - sh deploy.sh
3. Follow the instructions provided by AWS SageMaker to monitor and manage the deployed model.
