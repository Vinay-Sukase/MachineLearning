# Q1. Accept two numbers and print the greatest between them.

numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

if numb1 > numb2:
    print(f"{numb1} is greater than {numb2}")
else:
    print(f"{numb2} is greater than {numb1}")

# Q2. Accept the gender from the user as char and print the respective greeting message

gender = input("Please enter your gender (M or F): ")

if gender == 'M':
    print("Good morning Sir, Welcome to the class.")
elif gender == 'F':
    print("Good morning Madam, Welcome to the class")

# Q3. Accept an integer and check whether it is an even number or odd.

check_numb = int(input("Enter the number you want to check: "))

if check_numb % 2 == 0:
    print(f"{check_numb} is an even number.")
else:
    print(f"{check_numb} is an odd number.")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not ?

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age > 18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"Sorry {name} you cannot voter")

# Q5. Accept a year and check if it is a leap year or not.

year = int(input("Enter the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
