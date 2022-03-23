l = None
s = None

while True:
    n = raw_input("Enter a number: ")
    #print(type(n))
    if n == str("done"):
        break
    try:
        f = int(n)
    except:
        print("Invalid input")
        continue
    #print(f)
    if l is None:
        l = f
        s  = f
    elif f >= l:
        l = f
    elif f <= s:
        s = f    


print("Maximum is ",l)
print("Minimum is ",s)



