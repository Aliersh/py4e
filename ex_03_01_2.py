hrs=input("Enter hours: ")
rate=input("Enter rate per hour: ")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Please enter a correct number")
    quit()

if h<=40:
    tpay=h*r #Regular pay
else:
    rpay=40*r #Regular pay
    opay=(h-40)*(r*1.5) #Overrate pay
    tpay=rpay+opay #Total pay

print(pay)
