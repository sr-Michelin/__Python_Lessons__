from nltk.corpus import wordnet as wn

# Завдання №1 [Використовуючи визначення семантичної близькості, що базується на довжині шляху в графі WordNet, визначте
# які два поняття більш близькі за змістом «hostess» і «liberal» або «hostess» і  «host».]
print('Завдання №1'.upper())

Words = ['hostess.n.01', 'host.n.01', 'liberal.n.01']

s_1 = wn.synset(Words[0]).path_similarity(wn.synset(Words[2]))
s_2 = wn.synset(Words[0]).path_similarity(wn.synset(Words[1]))

print(f'Семантична близькість між "{Words[0]}" і "{Words[2]}": {s_1}')
print(f'Семантична близькість між "{Words[0]}" і "{Words[1]}": {s_2}')

if s_1 > s_2:
    print(f'Семантична близькість між {Words[0]} {Words[2]} є більшою ')
elif s_1 < s_2:
    print(f'Семантична близькість між {Words[0]} {Words[1]} є більшою')
else:
    print(f'Семантичні близькості є ідентичними')

# Завдання №2 [Методом Резника порахувати семантичну близькість між поняттями «host.n.01» і «sobersides.n.01».
# Для визначення інформаційного змісту використовуйте brown corpus]
print('\nЗавдання №2'.upper())
print('--підзавдання а [найменший спільний гіперонім]')

Words = ['host.n.01', 'sobersides.n.01']

min_hyp = wn.synset(Words[0]).lowest_common_hypernyms(wn.synset(Words[1]))
print(f'Найменший спільний гіперонім між {Words[0]} і {Words[1]}: {min_hyp}')

# b[Визначити IC даного найменшого спільного гіпероніма. IC (LCS ('host.n.01', 'sobersides.n.01'))]
#   I[Визначити список всіх понять, які є дочірніми вузлами знайденого найменшого спільного гіпероніма.
#     Можна отримати даний список вручну, використовуючи інтерфейс WordNet]

print('--підзавдання b [Визначити IC даного найменшого спільного гіпероніма. IC (LCS (host.n.01, sobersides.n.01))]')
print('---I[визначити список всіх понять, які є дочірніми вузлами знайденого найменшого спільного гіпероніма]')
min_hyp = str(min_hyp)
min_hyp = min_hyp[min_hyp.find("'") + 1: min_hyp.find("]") - 2]  # adult.n.01 з попереднього завдання

b1_hyp = wn.synset(min_hyp).hyponyms()
print(f'Гіпонім {min_hyp}: {b1_hyp}')

list_hyp = []
for hyp in b1_hyp:
    list_hyp.append(hyp.lemma_names())
print(f'Список лем гіпонімів: {list_hyp}')

list_words = []
for hyp in list_hyp:
    list_words.extend(hyp)

list_words.append('adult')

print(f'Список усіх понять, що є дочірними вузлами гіпоніма {min_hyp}: {list_words}')

#   II[Використовуючи brown corpus і формулу визначення інформаційного змісту, визначте інформаційний зміст
#      знайденого найменшого спільного гіпероніма]
print('---IІ[Використовуючи brown corpus і формулу визначення інформаційного змісту, визначте інформаційний зміст '
      'знайденого найменшого спільного гіпероніма]')
from nltk.corpus import brown

corpus_w = (' '.join(brown.words())).lower()
count_l = []

for word in list_words:
    counter = corpus_w.count(word)
    count_l.append(counter)
    print(f'{word}: {counter}')

print(f'Список входжень: {count_l}')

sum_counter = sum(count_l)
print(f'Частотна сума слів найменшого спільного гіпероніма: {sum_counter}')

w_in_br = len(brown.words())
print(f'Кількість слів у Brown corpus: {w_in_br}')

IC = sum_counter / w_in_br
print(f'Інформаційний вміст знайденого найменшого спільного гіпероніма: {IC}')

# c[Використовуючи формулу і десятковий або натуральний логарифм визначте simresnik («host.n.01», «sobersides.n.01»)]
import numpy as np

simresnik = -np.log(IC)
print(f'Семантична близькість за методом Резника: {simresnik}')

# Завдання №3 [розробити програмний додаток, яке розраховує методом Резника семантичну близькість будь-яких двох
# введених понять (або слів)]
print('\nЗавдання №3'.upper())
print('Програмний додаток, який розраховує методом Резника семантичну близькість будь-яких двохвведених понять')

word_0 = str(input('Введіть переше слово:'))
word_1 = str(input('Введіть друге слово:'))

# testing data
# word_0 = 'cat'
# word_1 = 'dog'

# перехід до видозміненої назви синтетів
word_0 += '.n.01'
word_1 += '.n.01'

# найменший спільний гіперонім
min_hyp = wn.synset(word_0).lowest_common_hypernyms(wn.synset(word_1))
print(f'Найменший спільний гіперонім між {word_0} і {word_1}: {min_hyp}')

# отримуємо всі елементи гіпонома
hyper_ = min_hyp[0].name()
hyponyms_ = wn.synset(hyper_).hyponyms()
print(f'list_hyp {hyper_} : {hyponyms_}')

# леми гіпономів
list_hyp = []
for h in hyponyms_:
    list_hyp.append(h.lemma_names())

print(f'Cписок лем гіпономів: {list_hyp}')

# список з першими лемами, які входять в гіпонім
list_words = []
for l in list_hyp:
    list_words.extend(l)

list_words.append(min_hyp[0].lemma_names()[0])
print(f'Cписок з першими лемами: {list_hyp}')

# ініціація Brown corpus
from nltk.corpus import brown

corpus_w = (' '.join(brown.words())).lower()
count_l = []

for word in list_words:
    counter = corpus_w.count(word)
    count_l.append(counter)
    print(f'{word}: {counter}')

print(f'Список входжень: {count_l}')

sum_counter = sum(count_l)
print(f'Частотна сума слів найменшого спільного гіпероніма: {sum_counter}')

w_in_br = len(brown.words())
print(f'Кількість слів у Brown corpus: {w_in_br}')

IC = sum_counter / w_in_br
print(f'Інформаційний вміст знайденого найменшого спільного гіпероніма: {IC}')

import numpy as np

simresnik = -np.log(IC)
print(f'Семантична близькість за методом Резника: {simresnik}')
