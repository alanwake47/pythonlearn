from datetime import date
import time
starttime = time.perf_counter()

#list empty
ldates = []
d1=date(2016,8,12)
d2=date(2018,7,12)
d3=date(2018,8,12)
d4=date(2019,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)

ldates.sort()

#time.sleep(3)

for d in ldates:
    print(d)

endtime = time.perf_counter()

print("executiontime",endtime-starttime)