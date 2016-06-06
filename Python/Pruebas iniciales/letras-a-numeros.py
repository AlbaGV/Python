Cs=raw_input("score: ")
Cs=float(Cs)
if Cs> 10: 
    print "Bad Input, try again"
elif Cs < 0:
    print "Bad Input, try again"
elif Cs < 6:
    print "F"
elif Cs >= 6 and Cs < 7:
    print "E"
elif Cs >= 7 and Cs < 8:
    print "D"
elif Cs >= 8 and Cs < 9:
    print "B"
elif Cs >= 9 and Cs >10:
    print "A"