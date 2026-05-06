list1=["Ahmad","Haider","Hassan","Talha","Ammar"]
# Access with index
print(list1[0])
print(list1[1])
# Access with negative index
print(list1[-1])
print(list1[-2])
# Access with range
print(list1[0:2])
print(list1[-3:-1])
# with only starting range
print(list1[2:])
print(list1[1:])
# with only ending range
print(list1[:2])
print(list1[:-2])
# Check if item exist
if "Ahmad" in list1:
    print("Yes")
if "Ali" in list1:
    print("Yes")
else:
    print("no")
# Check if not item exist
if "Anees" not in list1:
    print("Not exist")