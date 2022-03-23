try:
    num=int(input("Enter an even number: "))
    assert num%2==0, "You have entered odd number"
except AssertionError as obj:
    print(obj)
print("after assertion")