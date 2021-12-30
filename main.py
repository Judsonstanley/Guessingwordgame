import random
def luckynum():
    num=random.randint(1,10)
    return num

name=input("What is your name?")
n=luckynum()
print("hello"+name+\n 'Your lucky name is'+str(n))