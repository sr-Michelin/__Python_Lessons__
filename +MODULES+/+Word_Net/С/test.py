import pandas as pd  # модуль для роботи із таблицями
import nltk
import numpy as np  # математичний і статистичний модуль
import re  # оброблення регулярних виразів
from nltk.stem import wordnet  # для здійснення Лемматизації (приведення словоформи до її первісної словникової форми)
from sklearn.feature_extraction.text import \
    CountVectorizer  # викликання bow-методу (Bag of Words - вилучення об’єктів із текстових документів)
from sklearn.feature_extraction.text import \
    TfidfVectorizer  # викликання tfidf (оцінка важливості слова в контексті документа)
from nltk import pos_tag  # визначення частини мови
from sklearn.metrics import pairwise_distances  # обчислює відстані між відповідними елементами двох масивів.
from nltk import word_tokenize  # ділить рядок на підрядки шляхом розділення на вказаний рядок
from nltk.corpus import stopwords  # пошук стоп-слів

df = pd.read_excel('dialog_talk_agent.xlsx')  # проводим зчитування тестової бази даних (ТБД)
print(df[1:101])

print(df.shape[0], df.shape[1])  # вказуєм на розмір ТБД (стовпці, колонки)

df.ffill(axis=0, inplace=True)  # заповнюємо пусті ячейки попередніми значеннями (відтворення задуманого змісту таблиці)

df1 = df.head(10)  # копіюємо перші 10 рядків ТБД


# функція приведення тексту до нижнього регістру із подальшим видаленням спеціальних символів (залишаємо тільки текст)

def step1(x):
    for i in x:
        a = str(i).lower()
        p = re.sub(r'[^a-z0-9]', ' ', a)
        print(p)


print(step1(df1['Context']))  # опрацьовуємо першу колонку ТБД через функцію, подану вище

# токенізація слів
s = 'tell me about your personality'
words = word_tokenize(s)
print(f'\n{words}')

lemma = wordnet.WordNetLemmatizer()  # виклик лемматизації
print(f"\nВиклик лемматизації: {lemma.lemmatize('absorbed', pos='v')}")

print(f'Частини мови:{pos_tag(nltk.word_tokenize(s), tagset=None)}')  # знаходимо для токенізованих слів їх частини мови


# функція нормалізації тексту (приведення до виду, зручного для програмного опрацювання)
def text_normalization(text):
    text = str(text).lower()  # нижній регістр
    spl_char_text = re.sub(r'[^ a-z]', '', text)  # видалення спецсимволів
    tokens = nltk.word_tokenize(spl_char_text)  # токенізація
    lema = wordnet.WordNetLemmatizer()  # лемматизація
    tags_list = pos_tag(tokens, tagset=None)  # частини мови
    lema_words = []  # створюєм пустий список
    for token, pos_token in tags_list:
        if pos_token.startswith('V'):  # Дієслово
            pos_val = 'v'
        elif pos_token.startswith('J'):  # Прикметник
            pos_val = 'a'
        elif pos_token.startswith('R'):  # Прислівник
            pos_val = 'r'
        else:
            pos_val = 'n'  # Іменник

        lema_token = lema.lemmatize(token, pos_val)  # лемматизація
        lema_words.append(lema_token)  # доповнення лемматизованих слів  у lema_words

    return " ".join(lema_words)  # отримання повних речень із токенів (складаєм все назад)


print(
    f"Виклик функції нормалізації тексту: {text_normalization('telling you some stuff about me')}")  # тестовий виклик
# функції нормалізації тексту

df['lemmatized_text'] = df['Context'].apply(text_normalization)  # створення нового стопця із лемматизованих речень
print(df.head(5))

# вивід усіх стоп-слів (загальновживаних слів, що ігнорує система при індексуванні записів для пошуку)

stop = stopwords.words('english')
print(stop)

# Bag of words (bow)
print('\nBag of words (bow)')

cv = CountVectorizer()  # виклик count vectorizer
X = cv.fit_transform(df['lemmatized_text']).toarray()

# виведення усіх ункальних слів із ТБД

features = cv.get_feature_names()
df_bow = pd.DataFrame(X, columns=features)
print(df_bow.head())

Question = 'Will you help me and tell me about yourself more'  # тестовий запит

# переіврка присутності тестових слів

Q = []
a = Question.split()
for i in a:
    if i in stop:
        continue
    else:
        Q.append(i)
    b = " ".join(Q)

Question_lemma = text_normalization(b)  # нормалізація тестового запиту
Question_bow = cv.transform([Question_lemma]).toarray()  # виклик Bag of words

print(Question_bow)  # "мішок слів" для тестового запиту - матриця

# Подібність (cosine similarity)

# косинусна близькість для тестового запиту

cosine_value = 1 - pairwise_distances(df_bow, Question_bow, metric='cosine')
print(f'{cosine_value=}')

df['similarity_bow'] = cosine_value  # додаєм нову колонку для отриманих косинусних відстаней

df_simi = pd.DataFrame(df, columns=['Text Response', 'similarity_bow'])  # об'єднуємо ТБД із колонкою, поданою вище

df_simi_sort = df_simi.sort_values(by='similarity_bow',
                                   ascending=False)  # сортуєм значення колонки (у порядку спадання)

threshold = 0.2  # підбираємо значення збіжності і виводим найбільш відповідні рядки
df_threshold = df_simi_sort[df_simi_sort['similarity_bow'] > threshold]
print(df_threshold[:5])

index_value = cosine_value.argmax()  # індекс найбільного значення
print(index_value)

print('Питання - відповідь:')
print(Question)  # тестове запитання
print(df['Text Response'].loc[index_value])  # відповідь, взята із ТБД за індексом найбільної схожості

# Tf-idf (term frequency- inverse document frequency)
print('\nTf-idf (term frequency- inverse document frequency)')
Question1 = 'Tell me about yourself.'  # Тестове запитання №2

Question_lemma1 = text_normalization(Question1)  # нормалізація
Question_tfidf = tfidf.transform([Question_lemma1]).toarray()  # застосування tf-idf

tfidf = TfidfVectorizer()  # запуск tf-id для векторизації тексту
x_tfidf = tfidf.fit_transform(df['lemmatized_text']).toarray()  # перевід даних у масив

# отримуємо усі унікальні слова із їх рахунком

df_tfidf = pd.DataFrame(x_tfidf, columns=tfidf.get_feature_names())
df_tfidf.head()
