import os
#os.chdir(r'/Users/amankrishna/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/')
path = os.path.expanduser("~/Git/pythonlearn/Python for Everybody (Michigan)/Python Data Structures/")
fname = raw_input("Enter file name: ")
try:
    fh = open(path+fname, 'r')  
except:
    print('enter a valid filename')
    quit()


words = []
counts = {}
for line in fh:
    if line[:5] != "From ":
        continue
    else:
        words = line.split()
        counts[words[1]] = counts.get(words[1],0) +1

topc = None
topw = None
for key, value in counts.items():
    if topc == None or value>topc:
        topw = key
        topc = value

print(topw,topc)