def computepay(h, r):
    if h > 40:
        pay = h*r + (h-40)*r*0.5
    elif h>=0:
        pay = h*r
    else:
        print("Enter hours > 0")
        quit()
    return pay

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(h, r)
print("Pay", p)