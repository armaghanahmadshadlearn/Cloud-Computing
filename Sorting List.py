# Sort List Alphanumerically Acending
rana=["Rana Haider","Rana Ammar","Rana Talha","Armghan Ahmad"]
rana.sort()
print(rana)


# Sort List Alphanumerically decending
rana.sort(reverse=True)
print(rana)

# Customize Sort Function
def func(n):
    return abs(n-10) 

num=[12,21,43,213,543,123,53,10,234,65344,9]
num.sort(key=func)
print(num)


# Insensitative
list2=["Ali","ahmad","Armghan","Haider","talha"]
list2.sort()
print(list2)

list2.sort(key=str.lower)
print(list2)

# Reverse sorting
list2.reverse()
print(list2)