def main():
    listNum=[]
    x=0
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    nameCheck=input("Enter your name: ")
    if nameCheck in usernames:
        print("Access granted")
        while x < 5:
            num=float(input("Number: "))
            x+=1
            listNum.append(num)
        print("The first number is", listNum[0])
        print("The last number is", listNum[len(listNum)-1])
        print("The smallest number is",min(listNum))
        print("The largest number is", max(listNum))
        ave=sum(listNum)/len(listNum)
        print("The average of the number is",ave)
    else:
        print("Access denied")


main()