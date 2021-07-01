# Розиває список на елементи, потім їх склеює
# Позбавляє [],[]
m = ['Mike Shevcjenko', 'Vanya Golubosh']
m_join = ', '.join(m)
print(m, '\n', ', '.join(m))

s = str(m)
print('\n')
print(s.capitalize())  # копія строки із великими першими буквами
print(s.encode())
print(s.expandtabs(2))
print(s.isalnum())  # строка містить тільки цифрові символи
print(s.isalpha())  # строка містить тільки алфавітні символи
print(s.isidentifier())  # строка може бути індифікатором
print(s.islower())  # True, коли усі елементи у нижньому регітрі (print(s.isupper()) - навпаки)
print(s.isprintable())  # True,коли усі елементи друковані
print(s.isspace())  # True,коли усі елементи - пробіли
print(' S '.join('012'))  # обєднує елементи строки '012', ставлячи між ними ' S '
print(s.ljust(10))  # копія строки s, вирівнянна зліва на 10
print(s.replace(s[:0], s[:0]))  # заміна входення строки s[:0] в s строкою s[:0] --- без змін
print(s.split(s[0:6]))  # розбиття на менші елементи по аргументу, що у дужках
print(s.split(' '))  # розбиття на менші елементи за пробілом
print(s.splitlines())  # розбиття строки на менші за символами переводу
print(s.strip())  # видалення початкових і кінцевих відступів
print(s.swapcase())  # реверс "Caps lock"
print(s.title())  # Друк з великої букви
print(s.zfill(len(s) + 1))  # допоанення строки нулями спочатку за різницею аргумента і довжини обраної строки "s"
