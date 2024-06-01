# New York Housing Price Estimator
By: Leticia Genao

## Overview
This repository contains projects for predicting housing prices in New York City using machine learning techniques. The projects cover various deployment methods including Heroku, Docker, AWS SageMaker, and Kubernetes.

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
2. **Docker and AWS Deployment**: Dockerized version of the model deployed on AWS SageMaker Studio lab using containers.

## Repository Structure
- `/Part1_LocalDeployment`: Contains files for local model deployment and Heroku deployment.
- `/Part2_Docker_AWS_Deployment`: Includes Dockerfile and deployment instructions for AWS SageMaker.

## Usage
Detailed instructions for running and deploying the models are provided in each subdirectory.
