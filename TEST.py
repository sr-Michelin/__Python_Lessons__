class Person():
    name = None
    age = None
    money = None
    tell = None

    def __init__(self,name,age,money,tell):
        self.name = name
        self.age = age
        self.money = money
        self.tell = tell

class Teacher (Person):
    c = 'theoretical_ph'
    def set (self,name,age,money,tell,c):
        self.name = name
        self.age = age
        self.money = money
        self.tell = tell


YS  = Teacher (None,None,None,None)
YS.set('Юрій Степанович Криницький', 42, 100000, '068232425354','theoretical_ph')
print('Name = {0}, age = {1}, money = {2}, tell = {3}, c = {4}'.format(YS.name, YS.age, YS.money, YS.tell, YS.c))


