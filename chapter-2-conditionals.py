

#Exercise 3
try:
	hour = raw_input("Enter the hours you have worked:")
	hour = float(hour)
	if hour < 0:
		print "Hours couldn't be negative"
	else:
		rate = raw_input("Enter your rate:")
		rate = float(rate)
		if rate < 0:
			print "Rate couldn't be negative"
		else:
			if hour > 40:
				wage = (hour-40) * rate *(1+0.5) + 40 * rate
			else:
				wage = hour * rate
				
			print "your wage is",wage
except:
	print "Your input is wrong"

#Exercise 2
# number = raw_input("Enter one number between 0 and 10:")
# try:
	# number = int(number)
	# if number > 10:
		# print "Larger than maxinum"
	# else:
		# if number <0:
			# print "Smaller than the mininum"
		# else:
			# if number >= 8:
				# print "Cool"
			# elif number >= 6:
				# print "Good"
			# elif number >= 4:
				# print "Meh"
			# elif number >= 2:
				# print "Nevermind"
			# else:
				# print "Ouch!"
	
	
# except:
	# print "Error input"


#Exercise 1
# try:
	# age = raw_input("Enter your age:")
	# age = int(age)
	# print "you are",age,"years old"
# except:
	# print "Error input"