list1=[1,21,43,23,432,213]
list2=["A","B","C","D","F"]
# append()	Adds an element at the end of the list
list1.append(5)
print(list1)
# copy()	Returns a copy of the list
list3=[]
list3=list2.copy()
print(list3)
# count()	Returns the number of elements with the specified value
a=list2.count("A")
print(a)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
list1.extend(list2)
print(list1)
# insert()	Adds an element at the specified position
list1.insert(2, "E")
print(list1)
# pop()	Removes the element at the specified position
list1.pop(2)
print(list1)        
list1.remove("A")
print(list1)
# reverse()	Reverses the order of the list
list1.reverse()
print(list1)
# clear()	Removes all the elements from the list
list1.clear()
print(list1)
# index()	Returns the index of the first element with the specified value
a=list2.index("C")
print(a)
# remove()	Removes the item with the specified value
list2.remove("C")
print(list2)
