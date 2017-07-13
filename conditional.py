i = 8
if(i % 2):
	print "even numbers"
else:
	print "odd numbers"	



print "\n"

print 12 % 2

#using filter
def evens():
	numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
	print sum(filter(lambda x: not x%2, numbers))
	
evens()	


#using argument
def sum_evens():
	nums = [1,2,3,4,5,6,7,8,9,10,11,12]
	sum = 2+4+6+8+10+12
	print sum
	
sum_evens()	





num = [1,2,3,4,5,6,7,8,9,10,11,12]
result = 0
for item in num:
	 
    if not item%2:
             result += item         

print result


print "\n"


def get_age():
	age = (int)(raw_input("whats your age? "))
	if(age <12):
		print "you are a child"
	elif(age < 20):
		print "you are young"
	elif(age < 46):
		print "you are old"	
			

get_age()
get_age()



