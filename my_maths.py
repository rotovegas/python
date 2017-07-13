def calculate(op1, op2, f):
	
	
	if f == "add":
		return op1 + op2
		
	elif f == "substract":
		return op1 - op2
		
	elif f == "division":
		return op1 / op2
		
	elif f == "multiplication":
		return op1 * op2	
		

#declare the arguments

result = calculate(2, 5,"add")
resultsub = calculate(2,5,"substract")
resultdiv = calculate(2,5,"division")
resultmul = calculate(2,5, "multiplication")

#print out the results
print "Addition = " + str(result)
print "Substraction = " + str(resultsub)
print "Division = " + str(resultdiv)
print "Multiplication = " + str(resultmul)
print " "

#recomendation!
print "successful!"

