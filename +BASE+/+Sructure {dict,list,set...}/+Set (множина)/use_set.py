import sys

# Множина - невпорядкований набір простих об'єктів
# Створена для пошуку пересічень, належності

# Перевірка на входження:
print('Перевірка на входження:')
if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
    print('Help function is used...')

# Оброблення повторюючих елементів:
print('\nОброблення повторюючих елементів:')
seen = set()
IP = ['173.245.48.0/20', '103.21.244.0/22', '103.22.200.0/22', '03.31.4.0/22', '103.21.244.0/22']
for ip in IP:
    if ip not in seen:
        seen.add(ip)

        print(ip, end='; ')

# OR(!)
'''print('\n')
for ip in set(IP):
    print(ip, end='; ')'''

# Видалення потрібних елеметів:
print('\n\nВидалення потрібних елеметів:')
filenames = ['a.dat', 'b.dat', 'c.dat', 'd.dat', 'e.dat']
filenames = set(filenames)
for makefile in {'e.dat', 'd.dat'}:
    filenames.discard(makefile)
print(filenames)

# Генератори множин:
print('\nГенератори множин:')
files = ['a.html', 'dgd.htm', 'qwerty']
html = {x for x in files if x.lower().endswith(('.htm', '.html'))}
print(html)
