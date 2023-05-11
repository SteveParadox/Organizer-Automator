from nltk.chat.util import Chat, reflections
from tot import pairs
import nltk

#pairs = read_json('chat.json')

name = None
chat = Chat(pairs, reflections)

chat.converse()

