import sqlite3
import pandas

# Створення бази даних
dbase = sqlite3.connect('Our_data.db')
cursor = dbase.cursor()
print('Database opened')
print('Cursor created')

dbase.execute(''' CREATE TABLE IF NOT EXISTS e_m
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
BRANCH TEXT NOT NULL,
COURSE INT NOT NULL,
SSH INT NOT NULL) ''')
print('Table e_m created\n')


def insert_record(ID, NAME, BRANCH, COURSE, SSH):
    """Внесення даних"""
    # dbase.execute(''' INSERT INTO e_m (ID,NAME,BRANCH,COURSE,SSH) VALUES (4,'Sasha','physics', 5, 0) ''')
    dbase.execute(''' INSERT INTO e_m (ID,NAME,BRANCH,COURSE,SSH) VALUES (?,?,?,?,?)''',
                  (ID, NAME, BRANCH, COURSE, SSH))

    dbase.commit()
    print('REcord inserted')


# непряме внесення даних у таблицю через insert_record():
# insert_record(5,'Ivan','army', 0, 0)

def read_data():
    """Зчитування даних"""
    # data = dbase.execute(''' SELECT * FROM  e_m''')
    data = cursor.execute(''' SELECT * FROM  e_m''')  # більш швидший виклик даних
    for record in data:
        print(f'ID: {record[0]}, NAME: {record[1]}, BRANCH: {record[2]}, COURSE: {record[3]}, SSH: {record[4]}')


def check_data():
    """Вибіркове зчитування даних"""
    data = cursor.execute(''' SELECT * FROM e_m WHERE NAME = "Yara" ''')
    print('_' * 56)
    print('Checked collum:')
    for record in data:
        print(f'ID: {record[0]}, NAME: {record[1]}, BRANCH: {record[2]}, COURSE: {record[3]}, SSH: {record[4]}')


def check_fetch():
    """Вибіркове зчитування даних з умовою присутності даних через логічні оператори
    (на мою думку, більш надійіший спосіб)"""

    data = cursor.execute(''' SELECT * FROM  e_m WHERE NAME != "Ivan" ''')
    x = data.fetchall()
    print('_' * 56)
    print('Check_fetch:')
    # if x == []:
    if not x:
        print('Doesnt exist...')
    else:
        for record in x:
            print(f'ID: {record[0]}, NAME: {record[1]}, BRANCH: {record[2]}, COURSE: {record[3]}, SSH: {record[4]}')


def update_rec():
    """Перезапис даних"""
    dbase.execute(''' UPDATE e_m SET SSH = 1661 WHERE ID = 4 ''')
    dbase.commit()
    print('_' * 56)
    print('Updated...')


def dell_rec():
    """Видалення даних"""
    dbase.execute(''' DELETE FROM e_m WHERE ID = 0 ''')
    dbase.commit()
    print('Deleted ID = 0')


if __name__ == '__main__':
    read_data()
    check_data()
    update_rec()
    dell_rec()
    read_data()
    check_fetch()

dbase.close()
print('\nDatabase closed')
