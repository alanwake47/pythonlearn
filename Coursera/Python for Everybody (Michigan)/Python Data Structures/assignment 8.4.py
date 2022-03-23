import os
#os.chdir(r'/Users/amankrishna/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/')
path = os.path.expanduser("~/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/")
fname = raw_input("Enter file name: ")
try:
    fh = open(path+fname, 'r')  
except:
    print('enter a valid filename')
    print(fname)
    quit()

lst = list()
wrds = list()
for line in fh:
    wrds = line.split()
    for i in wrds:
        if i in lst:
            continue
        else:
            lst.append(i)
            
lst.sort()
print(lst)

    
#print(line.rstrip())
