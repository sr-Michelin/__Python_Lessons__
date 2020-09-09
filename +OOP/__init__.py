# Метод __init__ запускается, как только объект класса реализуется.
# Этот метод полезен для осуществления разного рода инициализации,необходимой для данного объекта

class Nor:
   def __init__(self,name):
       self.name = name
   def Say_hi(self):
       print('Hi',self.name)

Nor('Mike').Say_hi()

# or
'''n = Nor ('Mike')
n.Say_hi()'''


class Parson:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hello', self.name,'!')

p = Parson('Mike')
p.say_hi()


