import sqlite3
from random import randint

# Назва таблиці, ініціація
db = sqlite3.connect('server.db')
sql = db.cursor()

# Створення таблиці
sql.execute('''CREATE TABLE IF NOT EXISTS users  (
    login TEXT,
    password TEXT,
    cash BIGINT
)''')
# Підтверження зміни в т.
db.commit()


def reg():
    '''Функція реєстрації. Викликається для нових користувачів'''
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    # Запис отриманих реєстраційних даних у таблицю
    if sql.fetchone() is None:
        # sql.execute(f"INSERT INTO users VALUES ('{user_login}','{user_password}','{0}')")
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        db.commit()
        print('Зараєстровано!')
    else:
        print('Такий запис уже є!\n\nСписок зареєстрованих користувачів:')

        # Виклик списку зареєстрованих користувачів
        for value in sql.execute("SELECT * FROM users"):
            print(f"Login: {value[0]}, password: {value[1]}")


def caino():
    '''Функція привоєння певної грошової винагороди аипадковим учасникам лотереї'''
    user_login = input('Login: ')
    number = randint(1, 2)

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    # Якщо учасника лотереї немає у списку, викликається процес реєстрації
    if sql.fetchone() is None:
        print('The user with this login is\'nt exist. You should registered\n')
        reg()
    else:
        if number == 1:
            # Присвоєння 300 bucks:
            sql.execute(f"UPDATE users SET cash = {300} WHERE login = '{user_login}'")
            db.commit()
            print(f"{user_login} get 300 bucks!")

        else:
            print('You are lost=)\n')

# Вивід усіх учасників
def enter():
    print('\nAll users: ')
    for i in sql.execute("SELECT login,cash FROM users"):
        print(i)

# Запуск цього всого:
if __name__ == '__main__':
    caino()
    enter()
