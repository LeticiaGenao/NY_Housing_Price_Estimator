# New York Housing Price Estimator
By: Leticia Genao

## Overview
This repository contains projects for predicting housing prices in New York City using machine learning techniques. The projects explore various deployment methods, including Heroku, Docker, and AWS SageMaker, highlighting different stages and challenges encountered in deploying a machine learning model across multiple platforms.

## Problem Statement
In the complex landscape of the New York real estate market, accurately predicting housing prices is crucial for buyers, sellers, and investors alike. The "New York Housing Price Estimator" project utilizes machine learning to analyze various factors influencing house prices, enabling more informed decision-making. By considering attributes such as the number of bedrooms, bathrooms, square footage, and location, this model provides users with accurate price estimations, fostering transparency and efficiency in the real estate market.

## Data Source
The project utilizes the New York Housing Market dataset from Kaggle, comprising various features such as bedrooms, bathrooms, square footage, and location.
- [Data Source](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market/data)

## Background Info/Outside Research
The real estate market in New York City is notable for its volatility and complexity, with prices influenced by a myriad of factors including economic shifts, demographic changes, and zoning regulations. The COVID-19 pandemic introduced new dynamics, such as changes in homebuyer preferences and fluctuations in home inventory, which further complicated the market landscape. According to recent reports, residential housing market activity contributes significantly to the U.S. GDP, emphasizing the economic importance of accurate real estate valuation (Investopedia, 2024).

Despite a general upswing in prices, many New Yorkers face challenges such as "housing lock," where the scarcity of inventory and high mortgage rates discourage homeowners from selling. This project leverages advanced predictive modeling techniques to enhance the accuracy and reliability of real estate valuations, helping users navigate the complexities of the New York housing market more effectively.

## References
- [Spotlight: New York City’s Homeowner Housing Market](https://comptroller.nyc.gov/reports/spotlight-new-york-citys-homeowner-housing-market/)
- [Investopedia - Top U.S. Housing Market Indicators](https://www.investopedia.com/articles/personal-finance/033015/top-us-housing-market-indicators.asp)

## Projects
1. **Local Deployment and Heroku**: A Gradient Boosting Regression model deployed on Heroku for predicting housing prices in NYC.
   - [Heroku App](https://nyhouseprice-c155a038476a.herokuapp.com/)
2. **Docker Deployment**: The application is containerized and available for public access on Docker Hub.
   - [Docker Hub](https://hub.docker.com/r/leticiagenao/ny-house-price-estimator)
3. **AWS Deployment**: Initial setup on AWS includes the use of S3 for storage, ECR for Docker image management, and a SageMaker instance for model development. Full deployment on AWS is ongoing and aims for a robust, scalable solution.


## Repository Structure
- `/Part1_LocalDeployment`: Files for local deployment and Heroku, including Docker configuration.
- `/Part2_AWS_Deployment`: Contains documentation and screenshots illustrating the setup of AWS resources, with further deployment under development.

## Usage
Detailed instructions for running and deploying the models are provided in each subdirectory.

## Additional Resources
- **New York House Price Estimator.pdf**: Contains a PowerPoint overview of the project, detailing each phase from development to deployment and outlining the challenges encountered.
