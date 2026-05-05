import random
secnumber=random.randint(1, 100)
guess =0
print("Enter the number to guess:")

while guess!=secnumber:
    guess=int(input())
    if guess>secnumber:
        print("Your guess is greater than secret number")
    elif guess<secnumber:
        print("You guess is smaller than secret number")
    else:
        print("Your guess is correct Congratulations!")
