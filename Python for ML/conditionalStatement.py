# Conditional Statement
# Conditional Statements in Python allow decision-making by executing different blocks of code based on conditions

print("Welcome to Python Pizza Deliveries!")

size = input("What size of Pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Invalid input")

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is {bill}.")
