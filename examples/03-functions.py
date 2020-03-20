# Примеры функций и аргументов


def check_password(content):
    if content == "123123":
        print("Welcome")
    else:
        print("Error")


password = input("Enter password: ")
check_password(password)
check_password("000")
