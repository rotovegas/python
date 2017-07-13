for i in range(1,11):
	print i
# therefore, range is a set of numbers within a given numbers, of which the first is included and excluding the last number

print "\n"

for j in [1, 2, 3]:
	type(j)
	print j


print "\n"	

#to print the results of the above codes with range u ahve to asign the first number to 1 and the last number to 4
for a in range(1,4):
	print a


print "\n"

#to specify the intervals the last(2) is used to add efect to the results	
for d in range(1,7,2):
	print d


print "\n"
#range to return the list [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for r in range(0 ,19, 2):
	print r

print "\n"


# a function to produce (*****)-looping
def star():
	for a in range(0, 4):
		print "*****"
	
star()	

print "\n"

def moon():
	for g in range(0, 4):
		print "*" * g
	for h in range(4, 0, -1):
		print "*" * h	
				
		
moon()	
