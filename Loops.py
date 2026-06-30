fruits=["apple","mango","Pineapple"]
for i in fruits:
    print(i ,end="")

for i in range(5):
    print(i)

print("this is the new one")
for i in range(2,7):
    print(i,end='')

for i in range(7,2,-1):#works as i--
 print(i)

for i in "vakky":
   print(i,end="")

person={"set":12,"type":23,"name":"vakky"}
for key,value in person.items():
   print(key,":",value)


#while loops has started 
count =1;
while count<23:
   print(count)
   count+=1

while True:
   user=input("enter quite to go back:=")
   if(user=='quit'):
      print("user types quit ")
      break
   print("You typed:", user)

   #lets learn about break and continue

for i in range(10):
   if(i==4):
      break;
   print(i)

for i in range(10):
   if(i==4):
      continue;
   print(i)

fruits=["apple","mango","Pineapple"]
for index,value in enumerate(fruits):
   print(index,":",value)
   