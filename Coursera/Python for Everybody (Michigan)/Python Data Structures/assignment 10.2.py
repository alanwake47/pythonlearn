fname = input("enter file name:")

try:
    fh = open(fname,'r')
except:
    print("Enter a valid filename")
    quit()

hcount = {}
for line in fh:
    if line[:5] != "From ":
        continue
    else:
        words = line.split()
        hour = words[5].split(':')[0]
        hcount[hour] = hcount.get(hour,0)+1

for k,v in sorted(hcount.items()):
    print(k,v)