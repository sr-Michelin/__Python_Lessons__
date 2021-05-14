import pandas as pd
import nltk
import numpy as np
import re
from nltk.stem import wordnet  # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer  # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer  # to perform tfidf
from nltk import pos_tag  # for parts of speech
from sklearn.metrics import pairwise_distances  # to perfrom cosine similarity
from nltk import word_tokenize  # to create tokens
from nltk.corpus import stopwords  # for stop words

