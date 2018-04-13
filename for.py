from datetime import datetime

# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name

for (name, date, birthday, age) in BIRTHDAYS:
    if birthday == True:
        print("Happy Birthday " + name)
    else:
        pass


# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday

for (name, date, birthday, age) in BIRTHDAYS:
    birthdate = date.split('/') # Day / Month format
    for month in birthdate[1]:
        month = int(month) + 6
        if month > 12:
            month -= 12
            month = str(month)
            birthdate[1] = month
        else:
            month =str(month)
            birthdate[1] = month
        print(name, '/'.join(birthdate))


# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name

for (name, date, birthday, age) in BIRTHDAYS:
    birthdate = date.split('/') # Day / Month format
    for month in birthdate[1]:
        month =int(month)
        if month > 8:
            print(name)
        elif month < 7:
            print(name)


# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age

for (name, date, birthday, age) in BIRTHDAYS:
    if birthday == True and age <= 10:
        print(name + ' *' * age)
    else:
        pass

