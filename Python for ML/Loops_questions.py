from curses.ascii import isalpha, isdigit

# Q1. Accept an integer and Print hello world n times
numb = int(input("Enter a number: "))

for i in range(numb):
    print("Hello World")

# Q2. Print natural number up to n
numb = int(input("Enter a number: "))

for i in range(numb):
    if i != numb:
        print(i+1)

# Q3. Reverse for loop. Print n to 1
numb = int(input("Enter a number: "))

for i in range(numb,-1,-1):
    if i != numb:
        print(i+1)

# Q4. Take a number as input and print its table
numb = int(input("Enter a number: "))

for i in range(1,11):
    print(numb," x ",i,"=",numb*i)

# Q5. Sum up to n terms
numb = int(input("Enter a number: "))
sum = 0

for i in range(1,numb+1):
    sum += i

print(sum)

# Q6. Factorial of a number
numb = int(input("Enter a number: "))
fact = 1

for i in range(1,numb+1):
    fact *= i

print("Factorial =",fact)

# Q7. Print the sum of all even & odd numbers in a range separately
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))

even_sum = 0
odd_sum = 0

for i in range(start,end+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("The sum of the even numbers is:",even_sum)
print("The sum of the odd numbers is:",odd_sum)

# Q8. Print all the factors of a number
numb = int(input("Enter a number: "))
print("Factors: ")

for i in range(1,numb+1):
    if numb % i == 0:
        print(i)

# Q9. Accept a number and check if it's a perfect number or not
numb = int(input("Enter a number: "))
sum = 0

for i in range(1,numb):
    if numb % i == 0:
        sum += i

if sum == numb:
    print(f"{numb} is a perfect number")
else:
    print(f"{numb} is not a perfect number")

# Q10. Reverse a string without using in build functions
s = input("Enter a string: ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev += s[i]

print("Reversed string:",rev)

# Q11. Check string is Palindrome or not
s = input("Enter a string: ")
rev = ""
for ch in range(len(s)-1,-1,-1):
    rev =  rev + s[ch]

if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Q12.  Count all letters, digits, and special symbols from a given string
s = "P@#yn26at^&i5ve"
letters_count = 0
digits_count = 0
special_symbols_count = 0

for i in s:
    if isalpha(i):
        letters_count += 1
    elif isdigit(i):
        digits_count += 1
    else:
        special_symbols_count += 1

print(f"letters_count: {letters_count}")
print(f"digits_count: {digits_count}")
print(f"special_symbols_count: {special_symbols_count}")
