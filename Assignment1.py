# Question 1: Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Question 2: Check whether a number is even or odd
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Question 3: Find the greater of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")

# Question 4: Find the greatest of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)


# Question 5: Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Question 6: Check whether a year is a leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Question 7: Check if a character is a vowel or consonant
ch = input("Enter a character: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# Question 8: Check divisibility by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# Question 9: Check if a number is a multiple of both 3 and 7
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# Question 10: Assign grades based on marks
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# Question 11: Check uppercase or lowercase
ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet")
elif ch.isupper():
    print("Uppercase character")
else:
    print("Lowercase character")


# Question 12: Check vowel using if-elif
ch = input("Enter an alphabet: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
elif ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")


# Question 13: Check if three sides form a triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a > 0 and b > 0 and c > 0
        and a + b > c and a + c > b and b + c > a):
    print("Valid triangle")
else:
    print("Invalid triangle")


# Question 14: Determine the type of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a <= 0 or b <= 0 or c <= 0
        or a + b <= c or a + c <= b or b + c <= a):
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# Question 15: Find the largest among four numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest:", a)
elif b >= a and b >= c and b >= d:
    print("Largest:", b)
elif c >= a and c >= b and c >= d:
    print("Largest:", c)
else:
    print("Largest:", d)


# Question 16: Check whether a number is a three-digit number
num = int(input("Enter an integer: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# Question 17: Calculate electricity bill using slab rates
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", round(bill, 2))
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill: Rs.", round(bill, 2))
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    print("Electricity bill: Rs.", round(bill, 2))


# Question 18: Calculate income tax using sample income slabs
income = float(input("Enter annual taxable income (Rs.): "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 250000 * 0.05 + (income - 500000) * 0.10
else:
    tax = (250000 * 0.05
           + 500000 * 0.10
           + (income - 1000000) * 0.20)

if income >= 0:
    print("Income tax: Rs.", round(tax, 2))


# Question 19: Check whether a student passes all subjects
subjects = int(input("Enter number of subjects: "))

if subjects <= 0:
    print("Invalid number of subjects")
else:
    passed = True

    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i + 1}: "))

        if marks < 35 or marks > 100:
            passed = False

    if passed:
        print("Student has passed")
    else:
        print("Student has failed")


# Question 20: Check whether a number is within a given range
num = float(input("Enter a number: "))
lower = float(input("Enter lower limit: "))
upper = float(input("Enter upper limit: "))

if lower > upper:
    print("Invalid range")
elif lower <= num <= upper:
    print("Number is within the range")
else:
    print("Number is outside the range")


# Question 21: Simple calculator using if-elif-else
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# Question 22: Check whether a year is a century leap year
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year, but not a leap year")
else:
    print("Not a century year")


# Question 23: Determine the season based on month number
month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")
elif month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Summer")
elif month in (6, 7, 8, 9):
    print("Monsoon")
else:
    print("Post-monsoon / Autumn")


# Question 24: Find the number of days in a month
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or year < 1:
    print("Invalid month or year")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in (4, 6, 9, 11):
    print("30 days")
else:
    print("31 days")


# Question 25: Check whether a password meets minimum conditions
password = input("Enter a password: ")

if len(password) < 8:
    print("Password must have at least 8 characters")
elif not any(ch.isdigit() for ch in password):
    print("Password must contain a digit")
elif not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")
elif not any(ch.islower() for ch in password):
    print("Password must contain a lowercase letter")
else:
    print("Password meets the minimum conditions")


# Question 26: Determine ticket price based on age category
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Rs. 0")
elif age <= 17:
    print("Ticket price: Rs. 100")
elif age < 60:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 120")


# Question 27: Calculate discount based on purchase amount
amount = float(input("Enter purchase amount (Rs.): "))

if amount < 0:
    print("Invalid purchase amount")
elif amount >= 10000:
    discount = amount * 0.15
elif amount >= 5000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

if amount >= 0:
    print("Discount: Rs.", round(discount, 2))
    print("Final amount: Rs.", round(amount - discount, 2))


# Question 28: Check driving licence eligibility
age = int(input("Enter age: "))
eyesight = input("Is eyesight adequate? (yes/no): ").lower()

if age < 0:
    print("Invalid age")
elif age >= 18 and eyesight == "yes":
    print("Eligible to apply for a driving licence")
else:
    print("Not eligible under these conditions")


# Question 29: Login system with username and password validation
correct_username = "student"
correct_password = "Python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Invalid username")
else:
    print("Invalid password")


# Question 30: Menu-driven calculator using if-elif-else
print("----- Calculator Menu -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)
elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)
elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)
elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
elif choice == 5:
    print("Exiting calculator")
else:
    print("Invalid choice")
