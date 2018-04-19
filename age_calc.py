# Step 1
# Ask the user for their name and the year they were born.

name = input("What is your first name: ")
birth_date = input("What year were you born (YYYY)? ")

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.

age_25 = "{} you will be 25 in {}".format(name, (int(birth_date) + 25))
print(age_25)

age_50 = "{} you will be 50 in {}".format(name, (int(birth_date) + 50))
print(age_50)

age_75 = "{} you will be 75 in {}".format(name, (int(birth_date) + 75))
print(age_75)

age_100 = "{} you will be 100 in {}".format(name, (int(birth_date) + 100))
print(age_100)

# Step 3
# If they're already past any of these ages, skip them.

print("*************")
print("Print only ages and dates that I have not yet reached")
print("*************")

if (int(birth_date) + 25) > 2018:
    print(age_25)
else:
    pass
if (int(birth_date) + 50) > 2018:
    print(age_50)
else:
    pass
if (int(birth_date) + 75) > 2018:
    print(age_75)
else:
    pass
if (int(birth_date) + 100) > 2018:
    print(age_100)
else:
    pass