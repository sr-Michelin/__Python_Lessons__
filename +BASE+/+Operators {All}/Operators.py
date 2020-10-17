m = 1
n = 1

for i in range(10):
    print("M =",m, end=" ")
    print("N =",n)
    n = ~n
    m+=1

while True:
    q = input('\nВведіть щось: ')
    if len(q)==0:
        print('Кінець')
        break
    print('Довжина написаного: ',len(q))

type = 'Student'
age = 22
name = 'Mike'
sname = 'Shevchenko'
ssname = 'Sergiovich'
print('{0} {2} {3} {4} має {1} років(-и)'.format(type,age,name,sname,ssname))

print('dgdgd \
hhkjk')



