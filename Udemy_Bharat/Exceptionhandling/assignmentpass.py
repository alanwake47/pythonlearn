try:
    s=str(input("Enter password: "))
    assert len(s)>=8, "Entered password is less than 8 characters"
except AssertionError as obj:
    print(obj)
print("Enter password greater than 8 characters")