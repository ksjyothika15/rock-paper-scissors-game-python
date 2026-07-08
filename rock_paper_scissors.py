import random
choice=[0,1,2]
t=int(input("enter test cases:"))
for i in range(t):
    user_choice=int(input("enter '0' for rock , '1' for paper , '2' for scissor:"))
    comp_choice=random.randint(0,2)
    print(f"computers choice:{comp_choice}")
    if user_choice not in choice:
        print("invalid input from user!")
    elif comp_choice == user_choice:
        print("DRAW")
    elif (user_choice==0 and comp_choice==1) or (user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==0):
        print("computer wins")
    else:
        print("user wins")

print("Game over! thanks for playing")





