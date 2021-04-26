import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')


stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def BoW(tokenized_sentence, words):
    stemmed_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for index, word in enumerate(words):
        if word in stemmed_words:
            bag[index] = 1

    return bag
