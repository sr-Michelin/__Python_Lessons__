def reverse (text):
    return text [::-1]

def is_palindrome (text):
    return text == reverse(text)

smth = input('Ведіть текст: ')
if is_palindrome(smth):
    print('Ви ввели поліндром!')
else:
    print('Ви ввели не поліндром')