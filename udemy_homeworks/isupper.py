def upper_lower(str):
    d={"upper":0, "lower":0}
    for l in str:   
 	if l.isupper():
        	d["upper"]+=1
        elif l.islower():
                d["lower"]+=1
	else:
		pass
    print "Number of upper case letters:", d["upper"]
    print "Number of lower case letters:", d["lower"]	

upper_lower('Hello Mr. Rogers, how are you this fine Tuesday?')
