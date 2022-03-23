mat,phy,che=[float(x) for x in input("Enter M,P,C seprated by comma ").split(',')]
average=(mat+phy+che)/3
if mat < 35:
    print("You have failed in exam")
elif phy < 35:
    print("You have failed in exam")
elif che < 35:
    print("You have failed in exam")
elif average <= 59:
    print("C grade")
elif average <= 69:
    print("B grade")
else :
    print("A grade")
