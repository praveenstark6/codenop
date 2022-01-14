
"""
OPERATORS IN PYTHON

___________________________________________

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

___________________________________________

# Arithmetic operators

Arithmetic operators are used with 
numeric values to perform common
mathematical operations

+        Addition
-        Subtraction
*        Multiplication
/        Division
%        Modulus
**       Exponentiation
//       Floor division

Division and floor division
21 / 5 = 4.2 (float)
21 // 5 = 4 (integer)
___________________________________________
"""

print("(5 plus 6 is)", 5 + 6)

print("(5 minus 4 is)", 5 - 4)

print("(22 modulo 7 is)", 22 % 7) # remainder

print("(3 times 2 is)", 3 * 2)

print("(2 power 3 is)", 2 ** 3) # 2 X 2 X 2

print("(40 divided by 4 is)", 40 / 4)

print("(40 floor division by 4 is)", 40 // 4)


"""
______________________________________________
# Assignment operators
Assignment operators are used to assign
values to variables.

+=        Addition
-=        Subtraction
*=        Multiplication
/=        Division
%=        Modulus
**=       Exponentiation
//=       Floor division


old x value is 6
x += 2
new x value is 8
______________________________________________
"""

x = 5
print("Before Assignment operation:", x)
x //= 2
print("After Assignment operation:", x)

# x -= 2
# x *= 2
# x **= 2
# x /= 2
# x //= 2
# x %= 2

_____________________________________________

# Comparison Operators
print(1 == 1)
print(1 != 1)
print(5 < 6)
print(8 > 9)
print(90 <= 100)
print(7 >= 8)

_____________________________________________

# Logical Operators
a = 3
print(a < 12 and a > 78)

a = 4
print(a == 4 and a != 2)

print(a == 4 or a == 0)

print(not(a == 5))

_____________________________________________

# Identity Operators
a = [23]
b = [23]
print(a is b)
print(a is a)
print(a is not b)

_____________________________________________

# Membership Operators
print("b" in a)
print("z" not in a)
