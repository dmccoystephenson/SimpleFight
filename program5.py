from random import randint

yourDetails = {'Health': 100}
hisDetails = {'Health': 100}


running = True

while running == True:
	print "You punch your enemy!"
	
	hisDetails['Health'] = hisDetails['Health'] - (randint(1, 10))
	
	print "His health: %d" % hisDetails['Health']
	
	yourDetails['Health'] = yourDetails['Health'] - (randint(1, 10))
	
	print "Your health: %d" % yourDetails['Health']
	
	print " "
	
	if yourDetails['Health'] < 1:
		print "You died!"
		running = False
	
	elif hisDetails['Health'] < 1:
		print "He died!"
		running = False