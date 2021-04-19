import random
def main():
    number=int(input("How many quick pick? "))
    runtimes = 0
    while True:
        if runtimes == number:
            break
        else:
            lst=[]
            while len(lst) != 6:
                a = random.randint(1, 45)
                if a not in lst:
                    lst.append(a)
            b=sorted(lst)
            print("\n")
            for each in b:
                print("{:>2d}".format(each),end=' ')
            runtimes += 1