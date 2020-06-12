import re
finput=input('Enter file name: ')
fh=open(finput)
nlst=list()
su=0

for line in fh:
    line=line.rstrip()
    if re.findall('([0-9]+)',line): #Find all the lines with numbers
        line=re.findall('([0-9]+)',line) #Extract all numbers
        nlst=nlst+line #Make a list for all numbers

for num in nlst:
    inum=int(num)
    su=su+inum #Sumatory of all numbers

print('The sum of the numbers is',su)