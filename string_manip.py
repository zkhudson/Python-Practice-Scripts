# Step 1:
# Make two strings, each should be 8 characters long, made up of Xs and Os.
# First string should start with X, second string should start with O.
# Both strings should alternate between the two characters.
# You can use multiplication for this.

string_1 = 4 * "X0"
string_2 = 4 * "0X"

print(string_1)
print(string_2)

# Step 2:
# Make a list
# Add 1 of the X-started strings.
# Add 1 of the O-started strings.
# Repeat until you have 8 items total in the list.
# You can use multiplication for this, too.

my_list = []
x = 0
while x < 4:
    my_list.append(string_1)
    my_list.append(string_2)
    x += 1

print(my_list)

# Step 3:
# Print out the list of strings, joined with newlines \n.

print("\n".join(my_list))
