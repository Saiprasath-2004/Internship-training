target = 7

guess = int(input("Guess the number: "))

while guess != target:

    if guess < target:
        print("Too Low")

    else:
        print("Too High")

    guess = int(input("Guess again: "))

print("Correct! ,The target Number is:",target)