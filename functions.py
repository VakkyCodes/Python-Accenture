def starter():
    print("this is just a start")
starter();
def second(age):
    print("the age of mine is:-",age)
second(12)
def third(a,b):
    return a+b
print("the sum of two variable is ",third(12,2))

#main parts start here
def arg(*args):
    for i in  args:
        print(i)
arg("abbple","dff","asd") #this actually is used when we dont know how many parameters we have

def greet(name, message="Good Morning"):
    print(message + ",", name)

greet("Rahul")                    # Output: Good Morning, Rahul
greet("Priya", "Good Evening")   # Output: Good Evening, Priya

def student_info(name, age, city):
    print(name, age, city)

# Normal way (order matters)
student_info("Rahul", 22, "Hyderabad")

# Keyword way (order doesn't matter)
student_info(age=22, city="Hyderabad", name="Rahul")

def karg(**kargs):
    for key,value in  kargs.items():
        print(key,":-",value)
karg(name="Rahul", age=22, city="Hyderabad")

add = lambda a, b: a + b
print(add(3, 4))   # Output: 7

