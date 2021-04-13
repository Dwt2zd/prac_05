def main():
    password = get_password()
    aste=len(password)
    print(aste*"*")


def get_password():
    password = input("Set your password: ")
    return password


main()