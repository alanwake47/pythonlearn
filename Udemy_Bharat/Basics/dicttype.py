dict1={1:"Aman",2:"Aryan",3:"Susim"}
print(dict1)

print(dict1.values())

k=dict1.keys()
for i in k:
    print(i)

v=dict1.values()
for i in v:
    print(i)

print(dict1[3])

del dict1[2]
print(dict1)

country=["India", "Pakistan", "China"]
country.append("Bhutan")
del(country[2])
country.insert(2,"Nepal")
print(country)

countryset={"India","Pakistan","China"}
countryset.update({'Bhutan'})
countryset.remove("Pakistan")
countryset.add("Nepal")
print(countryset)
