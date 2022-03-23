import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f = open("myfile.txt","w")
    a,b=[int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c=a/b
    f.write("Writing %d into file" %c)
except ZeroDivisionError:
    print("division by zero not allowed")
    logging.error("Divsion by zero")
else:
    print("you have entered non zero number")
finally:
    f.close()
    print("File Closed")
    print("after exception")

    