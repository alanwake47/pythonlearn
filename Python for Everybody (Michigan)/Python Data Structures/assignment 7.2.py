# Use the file name mbox-short.txt as the file name
import os
os.chdir(r'C:\Users\Aman\Git\pythonlearn\Python for Everybody (Michigan)\Python Data Structures')

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('enter a valid filename')
    quit()

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        total += float(line[20:])
        #print(line)

print("Average spam confidence:",total/count)