a1 = [1,0,1,1,0]

if all(a1):
    print('Всі ел-ти "True" (1)')
else:
    print('Не всі ел-ти "True" (1)')

if any(a1):
    print('Хоча би один е-лт "True" (1)')

if any(a1) and not all(a1):
    print('Є "True" і "False"')
print('-------------------------------------')
a2 = [1,2,3,5,6,79,10,136,25,456]
n2 = 2
if any(num>n2 for num in a2):
    print('Є ел-ти, більші за %s'%n2)
if all(num>0 for num in a2):
    print('Усі цифри - додатні')
