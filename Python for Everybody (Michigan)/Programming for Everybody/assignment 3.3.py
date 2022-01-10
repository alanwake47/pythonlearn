score = float(input("Enter Score: "))

if score <= 1 and score >=0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")0.8
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Enter a score > 0")
else:
    print("please enter a score between 0.0 and 1.0")