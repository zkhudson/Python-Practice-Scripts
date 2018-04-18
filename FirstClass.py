# Step 1: Create a function named "add" that add two items
# after converting them to floats

# Step 2: Create a function named "multiple" that multiplies two items
# after converting them to floats

# Step 3: Use print, input, and your functions to collect numbers to
# multiply(add(), add()) and output the product

def convert(something):
    if '.' in something:
        try:
            return float(something)
        except ValueError:
            pass
    if something.isnumeric():
        try:
            return int(something)
        except ValueError:
            pass
    return something

# STEP 1
def add(value1, value2):
    return value1 + value2


# STEP 2

def multiple(value1, value2):
    return value1 * value2


# STEP 3

print("This script will add four numbers/letters and then multiple them. Please enter a number after each prompt...")

num1 = convert(input("Enter your first number: "))
num2 = convert(input("Enter your second number: "))
num3 = convert(input("Enter your third number: "))
num4 = convert(input("Enter your fourth number: "))


print(multiple(add(num1, num2), add(num3, num4)))
