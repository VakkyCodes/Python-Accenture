print("this is the starting of the python")
# no need to use semicolon or data type name
age=17
name="vakratund"
istrue=False
print("the name is :",name,"the age of ",name,age,"whatever is am saying is ",istrue)
#list is ordered and  changable ofc
fruit=["apple","rusbeery","mango"]
print(fruit)
fruit[1]="strawberry"
print("after changing mutation")
print(fruit)
mixed=[1,"mango",False]
print(mixed)
#tuple is again ordered but immutable
tuple=("name","order",12)
print(tuple)
# tuple[1]="or" this is error
#dictionary this is like key value pair
dict={
   "name":"vakky",
   "age":16,
   "place":"pune"
}
print(dict)
#set doesnt allow duplicate and is not ordered
set={12,'42323',"dfsfds",12}
print(set)

#now check data type
print(type(fruit))
#type conversion
x="10";
y=int(x);
print(type(x),type(y))
list=["name",12]
