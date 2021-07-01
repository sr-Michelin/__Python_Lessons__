import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from random import shuffle

# Вправа №1
print('\nВправа №1')


def gender_features(word):
    return {'last_letter': word[:2]}


names1 = ([(name, 'male') for name in names.words('male.txt')]) + \
         [(name, 'female') for name in names.words('female.txt')]
shuffle(names1)

featuresets = [(gender_features(n), g) for (n, g) in names1]
train_set = featuresets[500:]
test_set = featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Точність полученого класифікатора: ', nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

# Вправа №2
print('\nВправа №2')


def gender_features_comlex(name):
    features = {}
    features["firstletter"] = name[:3].lower()
    features["lastletter"] = name[-2:].lower()
    features["name length"] = len(name)
    return features


names_get2 = ([(name, 'male') for name in names.words('male.txt')] + \
              [(name, 'female') for name in names.words('female.txt')])
featuresets = [(gender_features_comlex(n), g) for (n, g) in names_get2]

train_set = featuresets[500:]
test_set = featuresets[:500]
classifier1 = nltk.NaiveBayesClassifier.train(train_set)
print('Точність отриманого класифікатора: ', nltk.classify.accuracy(classifier1, test_set))
classifier1.show_most_informative_features(5)

# Вправа №5
print('\nВправа №5\nАналіз помилок:')
train_names = names1[1500:]
devtest_names = names1[500:500]
test_names = names1[:500]

train_set = [(gender_features(n), g) for (n, g) in train_names]
devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
test_set = [(gender_features(n), g) for (n, g) in test_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))
errors = []

for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))
for (tag, guess, name) in sorted(errors):
    print('correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name))

print('Аналіз помилок:')
train_names = names_get2[1500:]
devtest_names = names_get2[500:1500]
test_names = names_get2[:500]

train_set = [(gender_features(n), g) for (n, g) in train_names]
devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
test_set = [(gender_features(n), g) for (n, g) in test_names]

classer = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classer, devtest_set))
errors = []

for (name, tag) in devtest_names:
    guess = classer.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))
for (tag, guess, name) in sorted(errors):
    print('correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name))
