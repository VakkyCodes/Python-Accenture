# 📦 PYTHON — Topic 5: Built-in Methods & List Comprehensions

# PART A: Common List Methods

# Examples are cleaned so explanatory text is commented and variable names are consistent.

pythonfruits = ["apple", "banana", "mango"]
# append() — add one item to the end
pythonfruits.append("orange")
print(pythonfruits)   # ['apple', 'banana', 'mango', 'orange']

# extend() — add multiple items (merges another list)
pythonfruits.extend(["grape", "kiwi"])
print(pythonfruits)   # ['apple', 'banana', 'mango', 'orange', 'grape', 'kiwi']

# append() vs extend() — classic interview question!
pythonlist1 = [1, 2, 3]
pythonlist1.append([4, 5])
print(pythonlist1)   # [1, 2, 3, [4, 5]]  ← added as ONE nested list item

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)   # [1, 2, 3, 4, 5]  ← each item added separately

# insert() — add item at a specific position
pythonfruits = ["apple", "banana", "mango"]
pythonfruits.insert(1, "papaya")   # insert "papaya" at index 1
print(pythonfruits)   # ['apple', 'papaya', 'banana', 'mango']

# remove() — remove by value
pythonfruits.remove("banana")   # removes first occurrence of "banana"
print(pythonfruits)   # ['apple', 'papaya', 'mango']

# pop() — remove by index (and returns the removed item)
pythonfruits = ["apple", "banana", "mango"]
removed = pythonfruits.pop(1)      # removes index 1
print(removed)               # banana
print(pythonfruits)                # ['apple', 'mango']

pythonfruits.pop()    # without index, removes the LAST item
print(pythonfruits)   # after popping last item

# sort() — sorts the list (modifies original)
pythonnums = [5, 2, 8, 1, 9]
pythonnums.sort()
print(pythonnums)   # [1, 2, 5, 8, 9]

pythonnums.sort(reverse=True)
print(pythonnums)   # [9, 8, 5, 2, 1]

# sorted() — returns a NEW sorted list (original unchanged)
pythonnums = [5, 2, 8, 1, 9]
new_nums = sorted(pythonnums)
print(new_nums)   # [1, 2, 5, 8, 9]
print(pythonnums)       # [5, 2, 8, 1, 9]  ← unchanged!

# reverse() — reverses list order
pythonnums = [1, 2, 3]
pythonnums.reverse()
print(pythonnums)   # [3, 2, 1]

# index() — find position of a value
pythonfruits = ["apple", "banana", "mango"]
print(pythonfruits.index("banana"))   # Output: 1

# count() — count occurrences of a value
pythonnums = [1, 2, 2, 3, 2, 4]
print(pythonnums.count(2))   # Output: 3

# len() — length of any collection
print(len([1,2,3]))     # 3
print(len("hello"))     # 5
print(len({"a": 1}))    # 1

# Slicing — extract part of a list/string
pythonnums = [10, 20, 30, 40, 50]
print(pythonnums[1:4])     # [20, 30, 40]  ← index 1 to 3 (4 excluded)
print(pythonnums[:3])      # [10, 20, 30]  ← from start to index 2
print(pythonnums[2:])      # [30, 40, 50]  ← from index 2 to end
print(pythonnums[-1])      # 50            ← last element
print(pythonnums[::-1])    # [50, 40, 30, 20, 10]  ← reversed!

# Syntax: list[start:stop:step]. Very commonly asked — practice this until it's automatic.

# PART C: Common Dictionary Methods
person = {"name": "Rahul", "age": 22}

person.keys()      # dict_keys(['name', 'age'])
person.values()    # dict_values(['Rahul', 22])
person.items()     # dict_items([('name', 'Rahul'), ('age', 22)])

person.get("name")          # "Rahul"
person.get("salary", 0)     # 0  ← default value if key doesn't exist (avoids error!)

person["salary"] = 50000    # adds a new key-value pair
person.update({"city": "Hyderabad"})   # adds/updates multiple pairs

person.pop("age")           # removes "age" key and returns its value

### PART D: `map()`, `filter()`, `zip()`

#### `map()` — applies a function to every item



nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)   # [1, 4, 9, 16]


#### `filter()` — keeps only items that pass a condition


nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]


#### `zip()` — combines two lists element-wise




names = ["Rahul", "Priya", "Amit"]
ages = [22, 25, 23]

combined = list(zip(names, ages))
print(combined)   # [('Rahul', 22), ('Priya', 25), ('Amit', 23)]

for name, age in zip(names, ages):
    print(name, age)