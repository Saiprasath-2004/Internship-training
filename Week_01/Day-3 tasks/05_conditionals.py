
# 1. Number Classifier

print("\n=== Number Classifier ===")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# 2. Grade Calculator

print("\n=== Grade Calculator ===")

score = int(input("\nEnter student's score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")



# 3. Login Validator

print("\n=== Login Check ===")

stored_password = "python123"

entered_password = input("\nEnter password: ")

if entered_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Password")


# 4. Largest Of Three Numbers

print("\n=== Largest Of Three Numbers ===")

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)