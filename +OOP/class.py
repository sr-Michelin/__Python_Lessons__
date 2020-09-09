class Person:
    def Say_Hi(self):
        print('Hello World!')

    def Func(self,x,y,z):
        res = x+y+z
        print('Сума:',res)
        print('')
        return res

p = Person ()
p.Say_Hi()

er = input('Напишіть "stop" для зупиненя циклу: ')
while True:
    if er == 'stop' or er == 'Stop' or er == 'STOP':
        print('Цикл зупнений! ')
        break

    try:
        p.Func(int(input('X: ')),int(input('Y: ')),int(input('Z: ')))
    except ValueError:
        print('Було введенно не число! ')