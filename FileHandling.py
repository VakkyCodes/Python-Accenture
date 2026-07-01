# 📁 PYTHON — Topic 7: File Handling
# Why File Handling?
# Programs often need to read/write files — CSVs, logs, configs.

# PART A: Opening a File — open()
file = open("data.txt", "r")   # opens file in read mode

# File Modes:
# "r" → Read (default)
# "w" → Write (overwrite)
# "a" → Append
# "r+" → Read & Write
# "x" → Create (error if exists)
# Add "b" for binary mode

# PART B: The with Statement (Best Practice!)

# ✅ Correct way
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File auto‑closes here

# PART C: Reading Files — 3 Ways
# Method 1: read()
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Method 2: readline()
with open("data.txt", "r") as file:
    line1 = file.readline()
    print(line1)

# Method 3: readlines()
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Looping line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# PART D: Writing to Files
# "w" mode — overwrite
with open("output.txt", "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")

# "a" mode — append
with open("output.txt", "a") as file:
    file.write("This is added at the end\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# PART E: Checking if a File Exists
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")

# Combining with Error Handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist!")
