import re
import tokenize
import nltk
import numpy as np
from nltk.corpus import brown, treebank

# Завдання 1
# Створюєм тестові дані та виконуємо тренування
print('\nЗавдання 1')
tree_tag_s = treebank.tagged_sents()
print(tree_tag_s)
size_ = int(len(tree_tag_s) * .9)
print(size_)
train_sents = tree_tag_s[:size_]
print(train_sents)
test_sent = tree_tag_s[size_:]

# Завдання 2
# Створюємо Unigram Tagger
print('\nЗавдання 2')
unigram_tg = nltk.UnigramTagger(train_sents)
print(f'Точність unigram: {unigram_tg.evaluate(test_sent)}')

# Створюємо Default Tagger
def_tg = nltk.DefaultTagger('NN')
print(f'Точність default tagge: {def_tg.evaluate(test_sent)}')

# Створюємо Bigram Tagger
big_tg = nltk.BigramTagger(train_sents)
print(f'Точність bigram tagger: {big_tg.evaluate(test_sent)}')

# Створюємо Combined Tagger
comb_tg = nltk.BigramTagger(train_sents)
t_0 = nltk.DefaultTagger('NN')
t_1 = nltk.UnigramTagger(train_sents, backoff=t_0)
t_2 = nltk.BigramTagger(train_sents, backoff=t_1)

print(f'Точність combined tagger: {t_2.evaluate(test_sent)}')

# Завдання 3
# Порівнюємо точність даних тегерів
print('\nЗавдання 3')


def acc_check(uni, bi, d, com):
    acc = [uni, bi, d, com]
    acc_np = np.array(acc)
    print(f'Досягнута максимальна точність: {acc_np.max()}')


acc_check(unigram_tg.evaluate(test_sent), def_tg.evaluate(test_sent), big_tg.evaluate(test_sent),
          t_2.evaluate(test_sent))

# Завдання 4
# Порівняйте точність даних тегерів з аналогічними, створеними на базі навчального корпусу 90% brown corpuus,
# категорії fiction.
print('\nЗавдання 4')

# Підготовка даних
brown_tg_sents = brown.tagged_sents(categories='fiction')
size_ = int(len(brown_tg_sents) * .9)
print(f'Розмір даних: {size_}')
train_sents_br = brown_tg_sents[:size_]
test_sents_br = brown_tg_sents[size_:]

# Створення Unigram Tagger для Brown
unigram_tg = nltk.UnigramTagger(train_sents_br)
print(f'Точність Unigram: {unigram_tg.evaluate(test_sents_br)}')

# Створення Default Tagger для Brown
def_tg = nltk.UnigramTagger(train_sents_br)
print(f'Точність Default: {def_tg.evaluate(test_sents_br)}')

# Створення Bigram Tagger для Brown
def_tg = nltk.BigramTagger(train_sents_br)
print(f'Точність Bigram: {big_tg.evaluate(test_sents_br)}')

# Створення Combined Tagger для Brown
t_0 = nltk.DefaultTagger('NN')
t_1 = nltk.UnigramTagger(train_sents_br, backoff=t_0)
t_2 = nltk.BigramTagger(train_sents_br, backoff=t_1)
print(f'Точність combined tagger: {t_2.evaluate(test_sents_br)}')

acc_check(unigram_tg.evaluate(test_sents_br), def_tg.evaluate(test_sents_br), big_tg.evaluate(test_sents_br),
          t_2.evaluate(test_sents_br))

# Завдання 5
# Порівняйте точність даних тегерів з аналогічними, створеними на базі навчального корпусу 90% brown corpuus,
# категорії fiction.
print('\nЗавдання 5')

# Створення файлу
from nltk.corpus import inaugural

washington_speech = inaugural.raw('1789-Washington.txt')
handle = open('Washington_sp', 'w')
handle.write(washington_speech)
handle.close()

# Остримання тексту
handle = open('Washington_sp', 'r')
get_sp = handle.read()


# Створення функції очищення тексту

def clear(text):
    text = re.sub(r'[\n]', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    return text


# Токенування реченнями
from nltk.tokenize import sent_tokenize, word_tokenize

speech = sent_tokenize(get_sp)
print(f'Текст промови: {speech}')

# Очищення тексту
cleaned_sp = []
for sp in speech:
    cleaned_sp.append(clear(sp))

print(cleaned_sp)

# Токенування для кожного речення
tokenized_sp = []
for sp in cleaned_sp:
    tokenized_sp.append(word_tokenize(sp))
print(f'Текст промови [токенізований для кожного речення]: {tokenized_sp}')

# Тегування за допомогою тренованого Brown - тагера
tagged_br = []

t_0 = nltk.DefaultTagger('NN')
t_1 = nltk.UnigramTagger(train_sents_br, backoff=t_0)
t_2 = nltk.BigramTagger(train_sents_br, backoff=t_1)

for t in tokenized_sp:
    tagged_br.append(t_2.tag(t))

print(f'Brown - тегування: {tagged_br}')

#  Тегування за допомогою тренованого Treebank - тагера
tagged_tree = []

t_0 = nltk.DefaultTagger('NN')
t_1 = nltk.UnigramTagger(train_sents, backoff=t_0)
t_2 = nltk.BigramTagger(train_sents, backoff=t_1)

for t in tokenized_sp:
    tagged_tree.append(t_2.tag(t))

print(f'Treebank - тегування: {tagged_tree}')

# Збереження промови у файл
# handle = open('Washington Brown tagded sp')
# handle.write(str(tagged_br))
# handle.close()

with open('Washington Brown tagded sp', 'w') as wsp:
    wsp.write(str(tagged_br))

with open('Washington Tree tagded sp', 'w') as wsp:
    wsp.write(str(tagged_tree))

# Завдання 6
# Створіть Combining backoff tagger на базі TrigramTag для будь-якого навчального корпусу. Оцініть точність його роботи.
print('\nЗавдання 6')
# Створення Trigraam - тегера
t_0 = nltk.DefaultTagger('NN')
t_1 = nltk.UnigramTagger(train_sents, backoff=t_0)
t_2 = nltk.BigramTagger(train_sents, backoff=t_1)
t_3 = nltk.TrigramTagger(train_sents, backoff=t_2)
print(f'Точність роботи тегера TrigramTag: {t_3.evaluate(test_sent)}')

# Завдання 7
# Збережіть навчений комбінований тегер, створений на базі treebank корпусу в файлі.
print('\nЗавдання 7\nЗаписуєм навчений комбінований тегер')

from pickle import dump, load

output = open('t3.pkl', 'wb')
dump(t_3, output, -1)

inp = open('t3.pkl', 'rb')
tagger = load(inp)
inp.close()

# Завдання 8
# Використовуйте цей збережений тегер для анотування невеликого англійського тексту.
print('\nЗавдання 8')
small_text = 'The Emperor of Mankind, often referred to by His faithful as the "God-Emperor," the "Master of Mankind," ' \
             'or simply "the Emperor," is the immortal Perpetual and psyker who serves as the reigning monarch of the ' \
             'Imperium of Man, and is described by the Imperial Ecclesiarchy and the Imperial Cult as the Father, ' \
             'Guardian and God of Humanity.'

small_text = clear(small_text)
print(small_text)
words = small_text.split(' ')
print(f'Текст, опрацьований збереженим тегуванням: {tagger.tag(words)}')

input()
