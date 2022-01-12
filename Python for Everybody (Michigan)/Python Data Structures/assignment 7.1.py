# Use words.txt as the file name

#os library helps us get current working directory (CWD)
import os
os.chdir(r'C:\Users\Aman\Git\pythonlearn\Python for Everybody (Michigan)\Python Data Structures')
fname = input("Enter file name: ")

try:
    fh = open(fname,'r')
except:
    print("Enter a valid filename")
    quit()
    
for i in fh:
    i_line = i.rstrip()
    print(i_line.upper())

