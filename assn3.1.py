#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.

#get the hours and rate from the user
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate per Hour:")
#convert them to float
h = float(hrs)
r = float(rate)

gross_pay = 0.0

#compute the gross pay
if h < 40:
	gross_pay = h * r
	
else:
	gross_pay = ( ( 40 * r ) + ( (h - 40) * 1.5 * r) )
print (gross_pay)
