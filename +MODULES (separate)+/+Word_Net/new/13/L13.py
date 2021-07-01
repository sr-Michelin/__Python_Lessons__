from nltk.corpus import stopwords
from collections import Counter
from nltk import tokenize
import collections
import math
import re

st = stopwords.words('english')


def tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = 1 + math.log10(tf_text[i])
    return tf_text


def idf(word, corpus):
    return math.log10(len(corpus) / sum([1. for i in corpus if word in i]))


def tfidf(corpus):
    doc_list = []

    for text in corpus:
        tf_idf_dict = {}
        computer_tf1 = tf(text)
        for word in computer_tf1:
            tf_idf_dict[word] = computer_tf1[word] * idf(word, corpus)
        doc_list.append((tf_idf_dict))

    return doc_list


corpus = []
t1 = open('13.1.txt', 'r').read()
clear_w1 = re.sub(r'\W', ' ', t1.lower())
w1 = tokenize.word_tokenize(clear_w1)
corpus.append(w1)

t2 = open('13.2.txt', 'r').read()
clear_w2 = re.sub(r'\W', ' ', t2.lower())
w2 = tokenize.word_tokenize(clear_w2)
corpus.append(w2)

t3 = open('13.3.txt', 'r').read()
clear_w3 = re.sub(r'\W', ' ', t3.lower())
w3 = tokenize.word_tokenize(clear_w3)
corpus.append(w3)

idf_get = tfidf(corpus)
max_idf = []
print(idf_get)
most_informative = []
dict_ = {}
for i in idf_get:
    dict_.update(i.items())
    most_common = Counter(dict_).most_common(20)
    for i in most_common:
        most_informative.append(i[0])

print(most_informative)
