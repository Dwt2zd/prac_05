def main():
    print("Temperatures converter")
    choice = get_choice()
    num = get_num()
    if choice == "C":
        C2F=9/5*num+32
        print("It in Fahrenheit is",C2F)
    elif choice =="F":
        F2C=5/9(num-32)
        print("It in Celsius is",F2C)
    else:
        print("Invalid input")


def get_num():
    num = float(input("Enter the temperatures: "))
    return num


def get_choice():
    choice = input("Select the inputting temperatures type: (C)Celsius or (F)Fahrenheit ").upper()
    return choice