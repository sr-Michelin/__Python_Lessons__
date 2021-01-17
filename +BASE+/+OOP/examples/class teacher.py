class teacher():
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment

    def discribe(self):
        print('Teacher {0} get {1} UAN every month'.format(self.name, self.payment))


list = [['A', 19000], ['B', 35000], ['C', 45000], ['D', 50000]]

for i in range(len(list)):
    teacher(list[i][0], list[i][1]).discribe()
