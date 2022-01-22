# -----------------------------------------------
# creating a function using "def" keyword in Python
# -----------------------------------------------

def wish(name):
    print("hello")

wish("praveen")

# -----------------------------------------------
# positional arguments while calling a function
# "name" is PARAMETER and "kevin" is ARGUMENT to that parameter
# -----------------------------------------------

def wish(name, age):
    print("hello", name)
    print("age:", age)

wish("kevin", 67)

# -----------------------------------------------
# keyword arguments while calling a function
# function_name(parameter1 = value1, parameter2 = value2)
# -----------------------------------------------

def wish(name, age):
    print("hello", name)
    print("age:", age)

wish(age=67, name="kevin")

# -----------------------------------------------
# setting default values to parameters of a function
# -----------------------------------------------

def wish(name="ben", age=18):
    print("hello", name)
    print("age:", age)

wish()

# -----------------------------------------------
# Return to use the output from a function
# -----------------------------------------------

def area(l, b):
    return l * b

print(area(4, 4) + 2)

# -----------------------------------------------
# passing n number of Arguments to a function 
# Here, arguments stored in a Tuple.
# -----------------------------------------------

def print_everything(*values):
    for value in values:
        print(value)

print_everything("helo", "tom", 76, [90,90])


def print_everything(*values):
    print(values)

print_everything("helo", "tom", 76)





