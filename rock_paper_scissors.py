import random
list1 = ["rock", "paper", "scissors"]
print("Game Started")
while True:
    a = input("Enter choice : ")
    a = a.lower()
    if a not in list1:
        print("enter correct option")
        continue
    b = random.choice(list1)
    print("Your choice =", a)
    print("Computer choice =", b)
    if a == b:
        print("same choice")
    else:
        if a == "rock":
            if b == "paper":
                print("computer wins")
            else:
                print("you win")
        elif a == "paper":
            if b == "scissors":
                print("computer wins")
            else:
                print("you win")
        else:
            if b == "rock":
                print("computer wins")
            else:
                print("you win")
    x = input("play again or not : ")
    if x != "yes":
        break
print("game over")