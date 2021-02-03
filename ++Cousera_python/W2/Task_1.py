import re
import pandas as pd
from scipy.spatial.distance import cosine

# Відкриття файла з текстом
with open('Task_1.txt', 'r') as f_sent:
    # with open('test.txt', 'r') as f_sent:
    d_sent = list(f_sent)

# Приведення до нижнього регістру
d_sent_lower = []
for i in range(len(d_sent)):
    d_sent_lower.append(d_sent[i].lower())

# Токенізація і видалення пустих слів
d_words = []
for line in d_sent_lower:
    d_words.append(re.split('[^a-z]', line))

d_words_cl = [[] for i in range(len(d_words))]
i = 0
for line in d_words:
    for word in line:
        if word != '':
            d_words_cl[i].append(word)
    i += 1

# Список усіх слів,таблиця
dict_words = {}
i = 0
for line in d_words_cl:
    for word in line:
        if word not in dict_words:
            dict_words[word] = i
            i += 1

frame_words = pd.DataFrame(dict_words, range(len(d_words_cl)))
f_rows, f_cols = frame_words.shape
print(f_rows, f_cols)

# занулення таблиці
for i in range(f_rows):
    for j in range(f_cols):
        frame_words.iloc[i, j] = 0

# присвоюєм теблиці frame_words по i,j кількість вхождень word у d_words_cl
for i in range(len(d_words_cl)):
    for word in d_words_cl[i]:
        frame_words.loc[i, word] += 1
print(frame_words)
# перевірка
frame_words.to_csv('Test.csv', header=1, index=None, sep=';')

# Косинусна відстань
dist_I_sent = []
for i in range(f_rows):
    dist_I_sent.append(cosine(frame_words.iloc[0], frame_words.iloc[i]))

print('\n{}'.format(dist_I_sent))

dist_I_sent_copy = list(dist_I_sent)
two_clses_val = [[-1, 0], [-1, 0]]

dist_I_sent_copy.remove(min(dist_I_sent_copy))  # Видалям 0 (перше знвчення)

for i in range(2):
    two_clses_val[i][w1] = min(dist_I_sent_copy)  # Знаходимо два найменших значень косинусної відстанні
    print('i-->', two_clses_val[i][1])
    for j in range(len(dist_I_sent)):
        if two_clses_val[i][1] == dist_I_sent[j]:  # Вказуєм на номер мінімальних значень
            two_clses_val[i][0] = j
    dist_I_sent_copy.remove(min(dist_I_sent_copy))  # Кожний раз видаляємо мінімум косинусної відстанні
    # (позбавлямося дублювання мінімумів у dist_I_sent_copy)
    print('Len -- ', len(dist_I_sent_copy))  # для перевірки

two_clses_val = sorted(two_clses_val)
print(two_clses_val)

# Запис у файл
with open('Task_1_answer.txt', 'w') as file_answer:
    for i in range(len(two_clses_val)):
        file_answer.write(str(two_clses_val[i][0]) + ' ')
