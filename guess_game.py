import random

print("Welcome to the Guess the Number Game!")
print("Take a number btw 1 to 100")
print("Guess it in few attempts as possible")

secret_number = random.randint(1,100)

attempts = 0
while True :
    guess = int(input("Guess the no btw 1 to 100: "))
    attempts += 1
    if guess < secret_number:
        print("Too low")

    elif guess > secret_number:
        print("Too High")

    else:
        print(f"You Nailed it! in {attempts} attempts.")
        break