#guessingwordgame
# list
import random
a=["apple","boy","bat","elephant","height","zoo","xylophone","no","open","jug","september"]
b = random.choice(a)
print(b)
# check if that alphabet is in the list

for i in range(0,len(b)):
    c = input("Enter your guess")
    d = b[i][0]
    e = c[0]
    print(e)
    print(d)
    if(d!=e):
        print("incorrect")
    elif(d==e):
        print("Next guess")
        break;
    else:
        print("game over")
        break;





