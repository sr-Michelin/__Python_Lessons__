import os

cwd = os.getcwd()
print(cwd)

'''python -m nuitka --mingw64 hello.py'''


def talk(message):
    return "Talk " + message


def main():
    print(talk("Hello World"))


if __name__ == "__main__":
    main()
