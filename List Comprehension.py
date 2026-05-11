# List Comprehension
rana=["Rana Haider","Rana Ammar","Rana Talha","Armghan Ahmad"]
list1=[]
for x in rana:
    if "Rana" in x:
        list1.append(x)
print(list1)


# Condition
rana=["Rana Haider","Rana Ammar","Rana Talha","Armghan Ahmad"]
list2=[x for x in rana if "Rana" in x ]
print(list2)


# Condition
list3=[x for x in rana if x=="Armghan Ahmad"]
print(list3)

list4=[x for x in rana]
print(list4)


# Iterable
list5=[x for x in range(12)]
print(list5)


# Iterable
list6=[x for x in (range (51))if x%5==0]
print(list6)


# Expression
list7=[x.upper() for x in rana]
print(list7)
list8=[x.lower() for x in rana]
print(list8)

list9=["Hello " for x in rana]
print(list9)

list10=[x if x!="Armghan Ahmad" else "Rana Hassan" for x in rana]
print(list10)