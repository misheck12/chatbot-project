import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SERVER_NAME = 'localhost:5000'  # Customize as needed
