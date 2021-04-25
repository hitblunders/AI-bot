# Intelligent chat bot program

# Import the libraries

from operator import length_hint
from nltk.translate.bleu_score import sentence_bleu
from newspaper import Article
import nltk
import random
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)


article = Article(
    'https://www.kidneyfund.org/kidney-disease/chronic-kidney-disease-ckd/')
article.download()
article.parse()

article.nlp()
corpus = article.text

print(corpus)


text = corpus
sentence_list = nltk.sent_tokenize(text)

print(sentence_list)


def greeting_response(text):
    text = text.lower()
    bot_greetings = ['hello', 'hola', 'hi', 'hey', 'howdy']

    user_greetings = ['wassup', 'hi', 'hey',
                      'greetings', 'hola', 'howdy', 'hello']

    for word in text.splot():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var

    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)

    similarity_scores = cosine_similarity(cm[-1], cm)

    similarity_scores_list = similarity_scores.flatten()

    index = index_sort(similarity_scores_list)
