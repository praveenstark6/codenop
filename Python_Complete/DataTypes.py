"""
Integer cannot contain decimal points.
Float cannot contain whole number (eg. 24.0)
Boolean starts with uppercase T and F (eg. True, False)
Strings should be inside quotes. 

List can contain duplicates.
Tuple can contain duplicates.
Set cannot contain duplicates.
dict key cannot contain duplicates

"34" -> String
 34  -> Integer
"""



a = 12
print(1, type(a))

a = -2.05
print(2, type(a))

a = True
print(3, type(a))

a = "45$%fcFG"
print(4, type(a))

a = ["adf", True, 1234, 12.45]
print(5, type(a))

a = [[4534], [False, 123]]
print(6, type(a))

a = ("Abdf", False, 56, 12.454)
print(7, type(a))

a = {"45", True, 56, 345.6}
print(8, type(a))

a = {1: "One", 2: "Two", 34: [3, 4]}
print(9, type(a))
