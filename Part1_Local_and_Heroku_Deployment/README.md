### Part1_LocalDeployment

**Overview**
This directory contains files for local model deployment and Heroku deployment. It includes the necessary code and configuration files to set up a Gradient Boosting Regression model for predicting housing prices in New York City.

**Contents**
- `app.py`: Python script for running the Flask web application.
- `requirements.txt`: List of Python dependencies required for running the application.
- `Dockerfile`: Configuration file for creating a Docker container.
- `finalized_model.pkl`: Serialized trained model for predicting housing prices.
- `Procfile`: Heroku configuration file specifying the commands to run the web application.
- `runtime.txt`: Specifies the Python version to be used on Heroku.

**Usage**
1. Install the required dependencies by running:
   - pip install -r requirements.txt
2. Run the Flask application locally by executing:
   - python app.py
3. Access the application at http://localhost:5000 in your web browser
4. For deploying to Heroku, follow the instructions provided in the main README.
5. For Docker:
   - Build the Docker image using: `docker build -t leticiagenao/ny-house-price-estimator .`
   - Run the container using: `docker run -p 5000:5000 leticiagenao/ny-house-price-estimator`

**Docker Deployment**: Dockerized version of the model deployed
   - [HDocker Hub](https://hub.docker.com/r/leticiagenao/ny-house-price-estimator)