x=int(input("Enter a number:"))
prime=True
for i in range(2,x-1):
    if x%i == 0:
        prime=False
        break
if (prime):
    print("The number is Prime")
else:
    print("The number is NOT Prime")
        
