def computepay(h, r):
    if h > 40:
        pay = h*r + (h-40)*r*0.5
    else:
        pay = h*r
    return pay

h = float(input("Enter Hours:"))
if h<0:
    print("Please Enter hours Greater than 0")
    quit()

r = float(input("Enter Rate:"))

p = computepay(h, r)
print("Pay", p)