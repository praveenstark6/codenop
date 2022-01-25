# len() function returns length of the string.
name = "code"

print(len(name))

# concatenation using + operator
name = "code"

print("I love" + name)

# multiplying to produce n number of concatened strings
print("-" * 30)

# number as string.
print("78" + "2")

# multi line strings using triple double quotes.
name = """
this 
is 
a 
multi line string.
"""

print(name)

name = """
name    age
___________
'max'      20
"phil"     22
"""

print(name)

name = "I love to Code!"
print(len(name))

# Indexing the string.
name = "I love to Code!"

print(name[2] + name[14])

# String Slicing               string[start : end : steps]
name = "I love to Code!"

print(name[2:7])

name = "I love to Code!"

print(name[2:7:2])

name = "I love to Code!"

print(name[-1:-6:-1])

# Reverse the entire string using [::-1] slicing.
name = "I love to Code!"

print(name[::-1])

# In and Not In operators 
name = "I love to Code!"

print("love" in name)

name = "I love to Code!"

print("z" not in name)

