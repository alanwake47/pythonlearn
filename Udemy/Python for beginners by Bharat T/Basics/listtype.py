lst=[10,20,"Aman",-10,30.5]

print(lst[3])
print(lst[3:5])
print(len(lst))

lst.append(4)
lst.remove("Aman")
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))
lst.insert(3,99)
print(lst)

lst.sort(reverse=True)
print(lst)
