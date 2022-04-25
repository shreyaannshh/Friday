import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer=PorterStemmer()
#Fridaysp= "hey", "hi"
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word=[stem(word) for word in tokenized_sentence]
    bag=np.zeros(len(words))
