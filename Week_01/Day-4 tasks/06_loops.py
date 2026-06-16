
##1. Multiplication Table


print("\n--- Multiplication Table ---")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



## 2. Sum 1-100


print("\n--- Sum 1 to 100 ---")

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)



## 3. FizzBuzz


print("\n--- FizzBuzz ---")

for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)



## 4. Guessing Game

print("\n--- Guessing Game ---")

target = 7

guess = int(input("Guess the number: "))

while guess != target:

    if guess < target:
        print("Too Low")

    else:
        print("Too High")

    guess = int(input("Guess Again: "))

print("Correct! You guessed the number.")