print()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('New person -  %s' % name)

    def tell_about_me(self):
        print('Name: %s, age: %s,:::,' % (self.name, self.age), end=' ')


class Student(Person):
    def __init__(self, name, age, course, money):
        Person.__init__(self, name, age)
        self.course = course
        self.money = money
        print('New student - %s' % self.name)

    def tell_about_me(self):
        Person.tell_about_me(self)
        print('course:  %s' % self.course, end=', ')
        print('have scholarship? %s' % self.money)


s1 = Student('Mike Shevchenko', 22, 5, 'Yes')
s2 = Student('Roman Kyrylyk', 21, 5, 'No')
s3 = Student('Kolya Gusev', 21, 5, 'Yes!!')
s4 = Student('Denys Ohrymovich', 21, 5, 'No')
s5 = Student('Jorik', 24, 5, 'No!')
s6 = Student('Yaryna Ostapchuk', 21, 5, 'Yes!!1!')

print()

list_ = [s1, s2, s3, s4, s5, s6]
for item in list_:
    item.tell_about_me()
