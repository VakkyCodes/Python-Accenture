age=118;
islie=True;
if(age!=18 and not islie):
    print("he can vote")
elif(age>20 or islie):
    print("ur wrong")
else:
    print("he can't vote")

#now talking about ternary operator
status="pass" if age>12 else "failed"
print(status)