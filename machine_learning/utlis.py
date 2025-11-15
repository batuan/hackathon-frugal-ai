import re

import contractions
import gensim
#from bs4 import BeautifulSoup

import numpy as np
np.set_printoptions(threshold=10000, suppress=True)
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

import pickle

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier, ClassifierChain
from sklearn.model_selection import train_test_split
from sklearn.metrics import hamming_loss, zero_one_loss
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, f1_score

def replace_contractions(text):
    """Supprime les contractions dans le texte."""
    return contractions.fix(text)

def replace_urls(text):
    """Supprime les URLs dans le texte."""
    return re.sub(r'http\S+', '<link>', text)

def remove_punctuation(text):
    """Supprime la ponctuation dans le texte."""
    return re.sub(r'[^\w ]', '', text)

def remove_non_ascii(text):
    """Supprime les caractères non ascii du texte."""
    return re.sub(r'[^\x00-\x7F]+', '', text)

def denoise_text(text):
    text = replace_urls(text)
    text = replace_contractions(text)
    text = remove_punctuation(text)
    text = remove_non_ascii(text)
    text = text.lower()
    return text

def remove_stopwords(text):
    """Remove stop words from list of tokenized words"""
    stop_words = stopwords.words('english')
    return [word for word in text if word not in stop_words]

def stem_words(text):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    return [stemmer.stem(word) for word in text]

def lemmatize_verbs(text):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos='v') for word in text]

def normalize(text):
    text = remove_stopwords(text)
    return text

def preprocess_text(text):
    text = denoise_text(text)
    # print(text)
    text = nltk.word_tokenize(text)
    text = normalize(text)
    text = stem_words(text)
    return ' '.join(text)
