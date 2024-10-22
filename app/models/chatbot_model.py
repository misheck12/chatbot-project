from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class CustomerServiceBot:
    def __init__(self):
        # Initialize the chatbot
        self.chatbot = ChatBot('CustomerSupportBot')
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

    def train_bot(self):
        # Train the bot with the English corpus
        self.trainer.train('chatterbot.corpus.english')

    def get_response(self, user_input):
        # Get a response to the user input
        response = self.chatbot.get_response(user_input)
        return response
