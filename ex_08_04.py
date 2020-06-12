fname=input('Enter file name:')
fh=open(fname)
lst=list()

for line in fh:
    line=line.rstrip()
    sl=line.split() #Split each line in a list
    lst=lst+sl #Concatenate all lists into one

lst.sort()

lstt=list()

for elm in lst:
    if elm not in lstt:
        lstt.append(elm)

print(lstt)