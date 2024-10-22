import unittest
from app.chatbot import customer_service_bot

class TestChatBot(unittest.TestCase):
    def test_bot_response(self):
        response = customer_service_bot.get_response("Hello")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
