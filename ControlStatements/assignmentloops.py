x=int(input("Enter number: "))

for i in range(1,x+1,1):
    if i % 10 == 0:
        continue
    if i>100:
        break
    print(i)