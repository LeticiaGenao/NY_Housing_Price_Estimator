from flask import Flask, request, render_template  # Import necessary Flask modules for web application
import pickle  # Import pickle for loading the machine learning model
import numpy as np  # Import numpy for numerical operations
import pandas as pd  # Import pandas for data manipulation
import os  # Import os for file and directory operations

app = Flask(__name__)  # Create a Flask web application instance

# Define the path to the saved machine learning model
model_path = os.path.join(os.path.dirname(__file__), 'finalized_model.pkl')

# Try to load the machine learning model from the specified path using pickle instead of joblib
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"Model file not found in {model_path}")  # Print an error message if the model file is not found
    raise  # Raise an exception to stop execution if the model file is not found

@app.route('/')  # Define a route for the home page of the web application
def home():
    """
    Renders the home page template.

    Returns:
        HTML template: Home page template.
    """
    return render_template('index.html')  # Render the home page template

@app.route('/predict', methods=['POST'])  # Define a route for receiving form data and making predictions
def predict():
    """
    Receives form data, preprocesses it, and makes predictions using the loaded model.

    Returns:
        HTML template: Home page template with prediction results or error message.
    """
    try:
        # Extract form data submitted via POST request
        borough = request.form['borough']  # Extract borough from form data
        p_type = request.form['type']  # Extract property type from form data
        bedrooms = float(request.form['bedrooms'])  # Extract number of bedrooms from form data and convert to float
        bathrooms = float(request.form['bathrooms'])  # Extract number of bathrooms from form data and convert to float
        square_feet = float(request.form['square_feet'])  # Extract square footage from form data and convert to float

        # Create a dictionary containing the extracted form data
        feature_dict = {
            'beds': bedrooms,
            'bath': bathrooms,
            'propertysqft': square_feet,
            'borough_Manhattan': 1 if borough == 'Manhattan' else 0,  # Encode borough as binary feature
            'borough_Queens': 1 if borough == 'Queens' else 0,  # Encode borough as binary feature
            'borough_Staten Island': 1 if borough == 'Staten Island' else 0,  # Encode borough as binary feature
            'borough_The Bronx': 1 if borough == 'The Bronx' else 0,  # Encode borough as binary feature
            'type_Condo': 1 if p_type == 'Condo' else 0,  # Encode property type as binary feature
            'type_House': 1 if p_type == 'House' else 0,  # Encode property type as binary feature
            'type_Multi-family': 1 if p_type == 'Multi-family' else 0,  # Encode property type as binary feature
            'type_Townhouse': 1 if p_type == 'Townhouse' else 0,  # Encode property type as binary feature
        }

        # Convert the dictionary to a pandas DataFrame
        features_df = pd.DataFrame([feature_dict])

        # Make predictions using the loaded machine learning model
        prediction = model.predict(features_df)
        output = format(prediction[0], ',.2f')  # Format the prediction for display with commas

        # Render the home page template with the prediction results
        return render_template('index.html', prediction_text=f'Estimated House Price: ${output}')
    except Exception as e:
        # Render the home page template with an error message if an exception occurs
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  #  default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
