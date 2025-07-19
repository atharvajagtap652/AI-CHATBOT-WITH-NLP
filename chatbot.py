import nltk
from nltk.chat.util import Chat, reflections

# Sample pairs of input patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how can I help you today?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]

# Start chatbot
def start_chat():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

start_chat()
