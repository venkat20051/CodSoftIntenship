import random
t=("rock","paper","sicissor")
p1=0
p2=0
r="yes"
while(True):
    if(r=="yes"):
        you=input("enter player1 choice:")
        com=random.choice(t)
        if(you=="rock" and com=="sicissor"):
            p1+=1
        elif(you=="paper" and com=="rock"):
            p1+=1
        elif(you=="sicissor" and com=="paper"):
            p1+=1
        elif(you==com):
            p1+=0
            p2+=0
        else:
            p2+=1
    else:
        print("Game Over:")
        break
    print("enter yes to continue game else no")
    r=input()
print("Player1 points are:",p1)
print("player2 points are",p2)
if(p1>p2):
    print("winner is player1")
elif(p1<p2):
    print("winner is player2")
elif(p1==p2):
    print("both have same points so there is no winner")

