fname=input('Enter file name:')
fh=open(fname)
mlst=list()
counts=dict()

for line in fh: #Create a list of each mail
    if line.startswith('From '):
        line=line.rstrip()
        line=line.split()
        mail=line[1]
        mlst.append(mail)

for mail in mlst: #Count mails
    counts[mail]=counts.get(mail,0)+1 

cmail=None
ctime=None
for mail,time in counts.items(): #Search for the max
    if ctime is None or time>ctime:
        cmail=mail
        ctime=time

print(cmail,ctime)