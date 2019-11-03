s={10,20,30,"XYZ",10,20}
print(s)
print(type(s))

s.update([88,99])

s.remove(30)
print(s)

f=frozenset(s)
print(f)
