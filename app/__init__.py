from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

from app import chatbot  # Import routes from chatbot.py
