import os
#os.chdir(r'/Users/amankrishna/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/')
path = os.path.expanduser("~/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/")
fname = raw_input("Enter file name: ")
try:
    fh = open(path+fname, 'r')  
except:
    print('enter a valid filename')
    quit()

word=()
count = 0
for line in fh:
    if not line[:5] == "From":
        continue
    else:
        count+=1
        word = line.split()
        print(word[1])
        
print("There were", count, "lines in the file with From as the first word")
