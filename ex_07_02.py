fname = input("Enter file name: ") #File "mbox-short.txt"
fh = open(fname)
count=0
su=0

for line in fh:
    if line.startswith ("X-DSPAM-Confidence:"):
        zpos=line.find('0') #Find the number in the line
        fnum=float(line[zpos:]) #Extract the number to a float number
        su=su+fnum #Sumatory of each value
        count=count+1 #Count of each value
    else:
        continue

print("Average spam confidence:",su/count)