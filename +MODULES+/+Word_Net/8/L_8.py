from nltk.corpus import wordnet as wn

# Вирішення проблеми відсутності програмних пакетів
# import nltk
# nltk.download()

# Завдання №1 [сінсети слова "dish"]
word = 'dish'
print('\nЗавдання №1'.upper())
print(f' Cінсети слова "dish":\n{wn.synsets(word)}')

# Завдання №2 [Визначення і приклад використання леми третього сінсета іменника і першого сінсета дієслова слова "dish"]
Words = ["dish.v.01", "dish.n.03"]
print('\nЗавдання №2'.upper(), end='')
for word in Words:
    print(
        f'\n Визначення леми сінсета {word}:\n{wn.synset(word).definition()}\n Приклад використання леми {word}:'
        f'\n{wn.synset(word).examples()}')

# Завдання №3 [Отримаєте всі імена, визначення та приклади використання сінсетів іменника "dish"]
print('\nЗавдання №3 [NOUN]'.upper())
for syn in wn.synsets('dish', wn.NOUN):
    print(f'І\'мя: {syn.name()}, визначення: {syn.definition()}, приклад: {syn.examples()}')

# Завдання №4 [Отримаєте всі імена, визначення та приклади використання сінсетів дієслова "dish"]
print('\nЗавдання №4 [VERB]'.upper())
for syn in wn.synsets('dish', wn.VERB):
    print(f'І\'мя: {syn.name()}, визначення: {syn.definition()}, приклад: {syn.examples()}')

# Завдання №5 [Отримайте лемму і ім/'я цієї леми будь-якого сінсета слова "dish"]
print('\nЗавдання №5 [lemmas]'.upper())
word = 'dish.n.03'
print(f'Лемма: {wn.synset(word).lemmas()}, і\'мя леми: {wn.synset(word).lemma_names()}')

# Завдання №6 [Отримаєте всі нижчестоящі і вищестоящі в родо-видовій ієрархії WordNet концепти першого сінсета іменника
# слова «work». Отримайте кореневий гіперонім даного концепту. Поясніть запис отриманих концептів.
print('\nЗавдання №6 [hyponyms]'.upper())
word = 'work.n.01'
print(f'Гіпонім {word}: {wn.synset(word).hyponyms()}')
print(f'Гіперонім {word}: {wn.synset(word).hypernyms()}')
print(f'Кореневий гіперонім {word}: {wn.synset(word).root_hypernyms()}')

#  Завдання №7 [За допомогою WordNet визначте з яких речовин складається "wood" (використовуйте першу лемму іменника
#  даного слова), і частиною яких речовин воно є.]
print('\nЗавдання №7 [substance]'.upper())
word = 'wood.n.01'
print(f'З яких речовин складається {word}: {wn.synset(word).substance_meronyms()}')
print(f'Частина мови {word}: {wn.synset(word).substance_holonyms()}')

# Завдання №8 [Отримайте антонім поняття "horizontal"]
print('\nЗавдання №8 [antonyms]'.upper())
word = 'horizontal.a.01.horizontal'
print(f'Антонім {word}: {wn.lemma(word).antonyms()}')

# Завдання №9 [Покажіть які дії залучені в поняття "eat"]
print('\nЗавдання №9 [entailments]'.upper())
word = 'eat.v.01'
print(f'Дії, залучені у {word}: {wn.synset(word).entailments()}')

# Завдання №10 [Знайдіть найменший спільний гіперонім сінсетів «bowl.n.02» і «polyhedron.n.01»]
print('\nЗавдання №10 [lowest_common_hypernyms]'.upper())
Words = ['bowl.n.02', 'polyhedron.n.01']
print(
    f'Найменший спільний гіперонім сінсетів {Words[0], Words[1]}: {wn.synset(Words[0]).lowest_common_hypernyms(wn.synset(Words[1]))}')

# Завдання №11 [Знайдіть найменший спільний гіперонім сінсетів «bowl.n.01» і «polyhedron.n.01»]
print('\nЗавдання №11 [lowest_common_hypernyms]'.upper())
Words = ['bowl.n.01', 'polyhedron.n.01']
print(
    f'Найменший спільний гіперонім сінсетів {Words[0], Words[1]}: {wn.synset(Words[0]).lowest_common_hypernyms(wn.synset(Words[1]))}')

# Завдання №12 [сайт, скріни]

# Завдання №13 [Визначте семантичну відстань між сінсетами job.n.07 і work.n.01]
print('\nЗавдання №13 [path_similarity]'.upper())
Words = ['job.n.07', 'work.n.01']
print(f'Семантична відстань між сінсетами {Words[0], Words[1]}: {wn.synset(Words[0]).path_similarity(wn.synset(Words[1]))}')

# Завдання №14 [Визначте семантичну відстань між сінсетами job.n.07 і job.n.07]
print('\nЗавдання №14 [path_similarity]'.upper())
Words = ['job.n.07', 'job.n.07']
print(f'Семантична відстань між сінсетами {Words[0], Words[1]}: {wn.synset(Words[0]).path_similarity(wn.synset(Words[1]))}')

# Завдання №15 [Визначте семантичну відстань між сінсетами job.n.07 і entity.n.01]
print('\nЗавдання №15 [path_similarity]'.upper())
Words = ['job.n.07', 'entity.n.01']
print(f'Семантична відстань між сінсетами {Words[0], Words[1]}: {wn.synset(Words[0]).path_similarity(wn.synset(Words[1]))}')
