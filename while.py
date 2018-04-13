# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

# Solution 1 here

while current_oven_temp < 350:
    print(current_oven_temp)
    current_oven_temp += 25

print("The Oven is Ready")


# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.

def total_and_average():
    numbers = []
    value = 0
    # Solution 2 here
    number = ''
    while number != 'q':
       number = input('Enter a number, or the letter q to quite...')
       if number == 'q':
           break
       else:
           numbers.append(number)
    print(numbers)
    for num in numbers:
        value = value + int(num)
    print(value)
    print(int(value/len(numbers)))


total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1

# Solution 3 here

while current <= 101:
    current += 1
    number = input('Enter a number: ')
    try: # Added some error handling in case someone enters a letter
        int(number)
        if int(number) % 3 == 0:
            print(number)
        elif int(number) % 5 == 0:
            print(number)
        else:
            pass
    except ValueError:
        print("Please only enter numbers...")
        pass