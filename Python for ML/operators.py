# OPERATORS :- operators are symbols that perform operations on variables and values.
# Python has several operators like arithmatic, comparison, logical operators and more

# ------------------------------------------------------------------------------------------------- #

# ARITHMETIC OPERATORS :- arithmetic operators perform mathematical operations
a = 15
b = 5

# ADDITION
add = a + b
print(add)

# SUBSTRACTION
sub = a - b
print(sub)

# MULTIPLICATION
mul = a * b
print(mul)

# DIVISION
div = a / b
print(div)

# FLOOR DIVISION
flr_div = a // b
print(flr_div)

# MODULUS
mod = a % b
print(mod)

# EXPONENTIAL
expo = a ** b
print(expo)

# ------------------------------------------------------------------------------------------------- #

#  ASSIGNMENT OPERATORS :-  Assignment operators are used to assign values to variables

# Basic assignment operator is =
a = 20

# COMPOUND ASSIGNMENT OPERATOR :- it combines arithmetic operations with assignment

# ADD and ASSIGN
a += 20
print(a)

# SUB and ASSIGN
a -= 20
print(a)

# MUL and ASSIGN
a *= 20
print(a)

# Div and ASSIGN
a /= 20
print(a)

# FloorDiv and ASSIGN
a //= 20
print(a)

# Mod and ASSIGN
a %= 20
print(a)

# Expo and ASSIGN
a **= 20
print(a)

# ------------------------------------------------------------------------------------------------- #

# COMPARISON OPERATOR :- are also called as relational operators, used to compare two values
# comparison operators provide Boolean result that is True and False
a = 15
b = 15

# equal to
print(a == b)

# not equal to
print(a != b)

# greater than
print(a > b)

# less than
print(a < b)

# greater than or equal to
print(a >= b)

# less than or equal to
print(a <= b)

# ------------------------------------------------------------------------------------------------- #
# ASCII value order

print(ord("A"))

print(ord("B"))

print("A" > "B")


# ------------------------------------------------------------------------------------------------- #

# Logical Operators :- are used to combine multiple conditions and return a Boolean result

# and :- Return True if both conditions are True

print((15 > 14) and (15 == (5*3)))  # Output : True and True = True
print((10/5==2) and (20/5==5))      # Output : True and False = False

# or :- Return True if at least one condition is True
print((12!=12) or (23 == 45) or (10>5)) # Output : False or False or True = True

# not :- Reverse the boolean value
print(not 12 == 12)

# ------------------------------------------------------------------------------------------------- #
