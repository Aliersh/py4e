sc=input(" Enter a score: ")
fsc=float(sc)

if fsc<=1.0: #Score evaluation to grades
    if fsc>=0.9: #Score higher than 0.9
        print("A")
    elif fsc>=0.8: #Score higher than 0.8
        print("B")
    elif fsc>=0.7: #Score higher than 0.7
        print("C")
    elif fsc>=0.6: #Score higher than 0.6
        print("D")
    else:
        print("F") #Score lower that 0.6

else:
    print("Enter a valid score") #Score out of range
    quit()
