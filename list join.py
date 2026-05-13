# using simple Addition symbol
list1=[1,21,43,23,432,213]
list2=["A","B","C","D","F"]
print(list1+list2)

# using loop 
for x in list2:
    list1.append(x)
print(list1)

# using extend function
list1=[1,21,43,23,432,213]
list2=["A","B","C","D","F"]
list1.extend(list2)
print(list1)
