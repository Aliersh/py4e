fname=input('Enter file name:')
fh=open(fname)
hlst=list()
counts=dict()

for line in fh:
    if line.startswith('From '):
        line=line.rstrip()
        line=line.split()
        time=line[5] #Get the time  
        time=time.split(':')
        hour=time[0] #Get the hour
        hlst.append(hour) #create a list of hours

for hr in hlst:
    counts[hr]=counts.get(hr,0)+1 #Counting the hours

shr=sorted(counts.items()) #Sorted dictionary with tuples

for h,t in shr:
    print(h,t)