import random
number = random.randint(0,100)
print("guess the magic number between 0, 100")
guess = -1
while guess!= number:
    guess = int(input("\nenter your guess"))
    if guess==number:
        print(f"yes, the number is {number}")
    elif guess > number:
        print("your guess is too high")
    else:
        print("your guess is too low")
    

    