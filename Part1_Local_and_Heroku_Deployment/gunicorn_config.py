# Gunicorn configuration file
import os

bind = "0.0.0.0:" + str(os.environ.get('PORT', 5000)) # Heroku automatically sets the PORT environment variable to 5000 if it isn't set, or to the host 0.0.0.0 on the port that the Gunicorn server is bound to. 
workers = 3 #This determines how many worker processes are needed to handle requests. 

