# LOOPS :- allow us to execute a block of code multiple times without rewriting it
# There are two types of loops For loop and WHILE loop

# increasing order
for i in range(1,16,1):
    print(i)

# decreasing order
for i in range(16,0,-1):
    print(i)

# increasing in negative
for i in range(-5,-15,-1):
    print(i)

# print the table
n = int(input("Enter the number you want table for: "))

for i in range(n,(n*10)+1,n):
    print(i)

# Loop on String
# Iteration using index value

user_str = input("Enter the string you want to find length of: ")
print(f"The length of the string is {len(user_str)}")

for i in range(len(user_str)):
    print(user_str[i])

# Iteration directly on the String
a = "NATURE"

for char in a:
    print(char)