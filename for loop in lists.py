# For loop in lists
list1=["Apple","Banana","Mango","Orange"]
for x in list1:
  print(x)
# For loop in lists using ranges
list1=["Apple","Banana","Mango","Orange"]
for i in range(len(list1)):
  print(list1[i])
# while loop in lists
list1=["Apple","Banana","Mango","Orange"]
i=0
while i<len(list1):
  print(list1[i])
  i=i+1
# Comprehension loop in lists 
list1=["Apple","Banana","Mango","Orange"]
[print(x) for x in list1]