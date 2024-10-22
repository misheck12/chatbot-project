from flask import request, render_template
from app import app
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the chatbot
customer_service_bot = ChatBot('CustomerSupportBot')

# Train the chatbot
trainer = ChatterBotCorpusTrainer(customer_service_bot)
trainer.train('chatterbot.corpus.english')

# Route for the chat interface
@app.route("/")
def index():
    return render_template("chat.html")

# Route to handle chatbot responses
@app.route("/get", methods=["POST"])
def get_bot_response():
    userText = request.form["msg"]
    return str(customer_service_bot.get_response(userText))
