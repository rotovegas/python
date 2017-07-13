def get_age():
	age = (int)(raw_input("whats your age? "))
	return age
	
	
def get_name():
		return raw_input("whats your name? ")
		

age = get_age()
name = get_name()


print "Hey, " + name + ", you are " + str(age) + " years old, dude!"		
