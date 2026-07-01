#Topic 6: Error Handling (try/except)

# PART A: Basic try/except
try:
    result = 10 / 0
except:
    print("Something went wrong!")

# Output: Something went wrong!

# PART B: Catching Specific Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Output: You can't divide by zero!



# Common Built-in Exceptions (Know these!)
# ZeroDivisionError → 10 / 0
# ValueError → int("hello")
# TypeError → "5" + 5
# IndexError → [1,2,3][10]
# KeyError → {"a":1}["b"]
# FileNotFoundError → open("missing.txt")
# NameError → print(undefined_var)
# AttributeError → "hello".append()

# Examples of each:
# ValueError
try:
    num = int("hello")
except ValueError:
    print("Cannot convert this to a number")

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Index doesn't exist in the list")

# KeyError
try:
    my_dict = {"name": "Rahul"}
    print(my_dict["age"])
except KeyError:
    print("This key doesn't exist in the dictionary")

# TypeError
try:
    result = "5" + 5
except TypeError:
    print("Cannot add a string and an integer")

# PART C: Multiple except Blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")

# Catching multiple exceptions in one block
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError):
    print("Either a division or value error occurred")

# PART D: else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Invalid number!")
else:
    print("Success! Result is:", result)
finally:
    print("This always runs, no matter what.")

# PART E: Raising Your Own Exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    withdraw(1000, 5000)
except ValueError as e:
    print("Error:", e)

# Output: Error: Insufficient balance!
