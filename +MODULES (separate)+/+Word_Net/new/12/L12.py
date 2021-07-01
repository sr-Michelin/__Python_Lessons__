import nltk
from nltk.corpus import gutenberg
from matplotlib import pyplot as plt

# Вправа №1
print('\nВправа №1')
william = nltk.Text(gutenberg.words(fileids='shakespeare-hamlet.txt'))
print(type(william))

# Вправа №2
print('\nВправа №2')
william.concordance('Hamlet')
print('Word Count - Hamlet', william.count('Hamlet'))

# Вправа №3
print('\nВправа №3')
print('General context of words "Hamlet", "Horatio"')
william.common_contexts(["Hamlet", "Horatio"])

# Вправа №4
print('\nВправа №4')
william.dispersion_plot(["Hamlet", "Horatio", "Ghost", "Polonius"])

# Вправа №5
print('\nВправа №5')
fdist = nltk.FreqDist(william)
print(len(fdist))
print(list(fdist))

# Вправа №6
print('\nВправа №6')
fdist.plot(50, cumulative=False)
fdist.plot(30, cumulative=True)

# Вправа №7
print('\nВправа №7')
print('Words that occur only once in the corpus')
print(fdist.hapaxes())

# Вправа №8
print('\nВправа №8')
a = [w for w in set(william) if len(w) > 5 and fdist[w] > 7]
b = [w for w in set(william) if len(w) < 3 and fdist[w] < 3]
print("A list of words longer than 7 character, the frequency of occurrence in the corpus", a)
print("A list of words longer than 3 character, the frequency of occurrence in the corpus", b)

# Вправа №9
print('\nВправа №9')


def lex():
    un = len(fdist)
    qu = fdist.N()
    lex = qu / un
    print("\n Lexical variety of text ", lex)


lex()

# Вправа №10
print('\nВправа №10')


def f(word, quantity):
    freq = william.count(word)
    fun = freq / quantity
    print(fun)
    return fun


quantity = len(william)
word = input("Enter the word: ")
prob = f(word, quantity)

# Вправа №11
print('\nВправа №11')
print('Collocations: ')
william.collocations()

# Вправа №12
print('\nВправа №12')
c = [w for w in set(william) if len(w) > 12]
print(f"A list of text words than are more than 12 character long \n{c}")

# Вправа №13
print('\nВправа №13')
word_length = nltk.FreqDist([len(w) for w in william])
print(f'Distribution of word length in the corpus {word_length.tabulate()}')

# Вправа №14
print('\nВправа №14')
print("Most common words", fdist.most_common(3))

# Вправа №15
print('\nВправа №15')
x = list(word_length.keys())
y = list(word_length.values())
width = 1
colors = ['red']
plt.bar(x, y)
plt.xlabel('Word length')
plt.ylabel('Word count')
plt.title('Word length diversity')
plt.show()

# Вправа №16
print('\nВправа №16')
print(f'Frequency of words: {word_length.keys()}')

# Вправа №17
print('\nВправа №17')
for key in list(word_length.keys()):
    print("%s -> %s" % (key, word_length[key]))
