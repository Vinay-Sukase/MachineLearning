# while loop :- The while loop repeats a block of code as long as a condition is True.
# It is useful when the number of iterations is unknown before execution.
import random

# numb = 1
#
# while numb < 10:
#     print(numb)  # This will run endlessly

# While loop questions

# Q1. Separate each digit of a number and print it on a new line
numb  = int(input("Enter a number: "))
while numb > 0:
    print(numb%10)
    numb = numb//10

# Q2. Accept a number and print its reverse.
numb = int(input("Enter a number: "))
numb_rev = 0
while numb > 0:
    numb_rev = numb_rev * 10 + numb % 10
    numb = numb//10

print(numb_rev)

# Q3. Accept a number and check if it is a palindrome number
numb = int(input("Enter a number: "))
numb_rev = 0
temp_numb = numb

while numb > 0:
    numb_rev = numb_rev * 10 + numb % 10
    numb = numb//10

if numb_rev == temp_numb:
    print(f"Number {numb_rev} is a palindrome")
else:
    print(f"Number {numb_rev} is not a palindrome")

# Q4. Create a random number guessing game in python
random_numb = random.randint(1,10)
guess = 0
while guess != random_numb:
    guess = int(input("Guess a number: "))
    if guess == random_numb:
        print("You guessed the number.")
    else:
        print("Your guess is wrong. \n Try again.")
