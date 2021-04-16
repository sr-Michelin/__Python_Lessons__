import pymorphy2

morph = pymorphy2.MorphAnalyzer()
morph_ukr = pymorphy2.MorphAnalyzer(lang='uk')
gr = morph.parse('блестящий')
print('1-6 завдання для російської мови')
for word in gr:
    print("tag: ", word.tag, ' norm form: ', word.normal_form, ' pos tag: ', word.tag.POS, ' cyr tag: ',
          word.tag.cyr_repr, ' score: ', word.score)
print(gr[0].tag)


def adj(word):
    # рід, число, відмінок
    print('рід, число, відмінок: ', word.tag.gender, word.tag.number, word.tag.case)


def prichastie(word):
    # вид, застава, час, перехідність
    print('вид, застава, час, перехідність: ', word.tag.aspect, word.tag.voice, word.tag.tense, word.tag.transitivity)


adj(gr[0])
prichastie(gr[0])

print('Твірний відмінок множ. числа: ', gr[0].inflect({'ablt', 'plur'}))
print("Лексема: ", gr[0].lexeme)
print("Лексема: ", gr[2].lexeme)

file = open("ru.txt", "r", encoding='utf8')
text = file.read().split()
file.close()
tokens = [w.lower() for w in text if w.isalpha()]
f = open('results.txt', 'w')
for word in tokens:
    gr = morph.parse(word)
    f.write(word + ' ' + str(gr[0].tag.POS) + '\n')
f.close()
print('1-6 завдання для української мови')
gr_ukr = morph_ukr.parse('привітний')
for word in gr_ukr:
    print("tag: ", word.tag, ' norm form: ', word.normal_form, ' pos tag: ', word.tag.POS, ' cyr tag: ',
          word.tag.cyr_repr, ' score: ', word.score)
print(gr_ukr[0].tag)
adj(gr_ukr[0])
prichastie(gr_ukr[0])
print("Створює відмінок мнж. числа: ", gr_ukr[0].inflect({'ablt', 'plur'}))
print("Лексема: ", gr_ukr[0].lexeme)
file_ukr = open("ua.txt", "r", encoding='utf8')
text_ukr = file_ukr.read().split()
file_ukr.close()
tokens_ukr = [w.lower() for w in text_ukr if w.isalpha()]
f_ukr = open('results_ukr.txt', 'w')
for word in tokens_ukr:
    gr = morph_ukr.parse(word)
    f_ukr.write(word + ' (' + str(gr[0].tag.cyr_repr) + ')\n')
f_ukr.close()

input()