import math
import random

# Global Variables:

# Current time variable
t = 0.0

# Time of line switch
ts = math.inf

# Initialize departure times
td1 = math.inf
td2 = math.inf
td3 = math.inf
td4 = math.inf
td5 = math.inf


# Closing time variable
tc = 5.0

# Initialize line lists
# Line lists will contain customers represented by an integer number of items in cart
line1 = list()
line2 = list()
line3 = list()
line4 = list()
line5 = list()

# Total number of customer arrivals throughout the day
totalArrivals = 0

# Initialize r.v. generation parameters

# Arrival time parameter
lam = 0.5

# Cart size parameter
cartSizeLam = 0.5

# Generates arrival time, along with number of items in cart
def generateArrivalTime():
	global t
	# Non-homogenous Poisson distribution
	# random variable u
	u = random.random()
	# Set New Arrival time to exponential equation
	Y = (-lam) * math.log(1 - u)
	return Y + t


# TODO: change to weibull
def generateDepartureTime():
	global t
	# If customer is at the front of the line -> generate departure time using weibull dist.
	u = random.random()
	Y = (-lam) * math.log(1 - u)
	return Y + t

# Exponential
def generateSwitchTime():
	u = random.random()
	Y = (-switchLam) * math.log(1 - u)
	return (Y + t)

#Parker
def getItemsInCart(line):
	# Return number of items in first current customer's cart (first customer in line)
	return line[len(line) - 1].numItems

#Jack
# Generated by exponential random variable (?)
# Should return an integer
def generateItemsInCart():

	# Generate uniform random variable
	u = random.random()

	# Returns number of items in cart 
	return math.ceil(40*(-cartSizeLam)*math.log(1 - u))

#Eric
def getEstimatedWaitTime(line):
	# Returns line (which is a list)
	sum = 0
	i = 0
	for i in range(len(line) - 1):
		sum += line[i]
	return sum + (5 * len(line))

# Returns shortest estimated line
# Return value is the line that the customer chooses
def chooseLine(numItems):

	global line1, line2, line3, line4, line5

	if (numItems <= 10):
		if min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4), getEstimatedWaitTime(line5)) == getEstimatedWaitTime(line1):
			print "Line 1 chosen"
			return 1
		elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4), getEstimatedWaitTime(line5)) == getEstimatedWaitTime(line2):
			print "Line 2 chosen"
			return 2
		elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4), getEstimatedWaitTime(line5)) == getEstimatedWaitTime(line3):
			"Line 3 chosen"
			return 3
		elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4), getEstimatedWaitTime(line5)) == getEstimatedWaitTime(line4):
		else: 
			print "Line 5 chosen"
			return 5
	else: 
		if min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line1):
			print "Line 1 chosen"
			return 1
		elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line2):
			print "Line 2 chosen"
			return 2
		elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line3):
			"Line 3 chosen"
			return 3
		else:
			print "Line 4 chosen"
			return 4

def getNextEvent():
	global ta, td1, td2, td3, td4
	return min(ta, td1, td2, td3, td4)

def getLongestLine():
	return max(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4))

def getShortestLine():
    return min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4))

def getShortestLineSwitch(line):
	return min(getEstimatedWaitTime(line), getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4))

def printTime():
	global t
	print "Current time:", t

def printNumCustomersInLine():
	global line1, line2, line3, line4
	print "# of customers in line 1:", len(line1)
	print "# of customers in line 2:", len(line2)
	print "# of customers in line 3:", len(line3)
	print "# of customers in line 4:", len(line4)

def printDepartureTime(line):
	if (cmp(line, line1)):
		print "Line 1 Departure Time:", td1
	elif (cmp(line, line2)):
		print "Line 2 Departure Time:", td2
	elif (cmp(line, line3)):
		print "Line 3 Departure Time:", td3
	elif (cmp(line, line4)):
		print "Line 4 Departure Time:", td4

# Main loop
def runSimulation():

	global t, ta, td1, td2, td3, td4, ts, tc
	global line1, line2, line3, line4
	global totalArrivals, lam, cartSizeLam

	# Initialize first arrival time
	ta = generateArrivalTime()

	while (t < tc):
		# Case 1 (Arrival occurs before departure from any line and before closing):
		if (getNextEvent() == ta and ta < tc):

			# Update current time by time of arrival
			t = ta
			printTime()

			# Increment total arrivals by 1
			totalArrivals += 1

			# Add customer to "shortest" line
			items = generateItemsInCart()
			if (chooseLine() == 1):
				line1.append(items)
			elif (chooseLine() == 2):
				line2.append(items)
			elif (chooseLine() == 3):
				line3.append(items)
			else:
				line4.append(items)

			printNumCustomersInLine()

			# Generate and set new arrival time
			ta = generateArrivalTime()
			print "Next arrival time:", ta

			if (len(line1) == 1):
				td1 = generateDepartureTime()
				print "Line 1 Departure Time:", td1
			elif (len(line2) == 1):
				td2 = generateDepartureTime()
				print "Line 2 Departure Time:", td2
			elif (len(line2) == 1):
				td3 = generateDepartureTime()
				print "Line 3 Departure Time:", td3
			elif (len(line4) == 1):
				td4 = generateDepartureTime()
				print "Line 4 Departure Time:", td4

			print "Next event time:", getNextEvent()
			t = getNextEvent()
			printTime()

		# Case 2 (Departure from line 1):
		elif (getNextEvent() == td1 and td1 < tc):

			# Update current time by earliest departure time
			t = td1
			printTime()

			# Remove departed customer from line with earliest departure time
			line1.pop(0)
			printNumCustomersInLine()


			if (len(line1) > 0):
				td1 = generateDepartureTime()
			else: 
				td1 = a_jillion

		# Case 3 (Departure from line 2):
		elif (getNextEvent() == td2 and td2 < tc):

			# Update current time by earliest deparature time
			t = td2
			printTime()


			# Remove departed customer from line with earliest departure time
			line2.pop(0)

			printNumCustomersInLine()


			if (len(line2) > 0):
				td2 = generateDepartureTime()
			else: 
				td2 = a_kajillion

		# Case 4 (Departure from line 3):
		elif (getNextEvent() == td3 and td3 < tc):

			# Update current time by earliest deparature time
			t = td3
			printTime()

			# Remove departed customer from line with earliest departure time
			line3.pop(0)

			printNumCustomersInLine()


			if (len(line3) > 0):
				td3 = generateDepartureTime()
			else: 
				td3 = a_jillion

		# Case 5 (Departure from line 4):
		elif (getNextEvent() == td4 and td4 < tc):

			# Update current time by earliest departure time
			t = td4
			printTime()

			# Remove departed customer from line with earliest departure time
			line4.pop(0)

			printNumCustomersInLine()

			if (len(line4) > 0):
				td4 = generateDepartureTime()
			else: 
				td4 = a_jillion


		# Case 7 (Next departure happens after closing and at least one customer is still in line)
		elif ((tc < getNextEvent()) and ((len(line1) + len(line2) + len(line3) + len(line4)) > 0)):

			# Keep out new arrivals
			ta = a_kajillion

			t = getNextEvent()
			if (getNextEvent() == td1 and len(line1) > 0):
				line1.pop(0)
				td1 = generateDepartureTime()
			
			elif (getNextEvent() == td2 and len(line2) > 0):
				line2.pop(0)
				td2 = generateDepartureTime()

			elif (getNextEvent() == td3 and len(line3) > 0):
				line3.pop(0)
				td3 = generateDepartureTime()

			elif (getNextEvent() == td4 and len(line4) > 0):
				line4.pop(0)
				td4 = generateDepartureTime()
				

		# Case 8 (Closing time is earlier than next departure and all lines are empty):	
		elif (tc < getNextEvent() and ((len(line1) + len(line2) + len(line3) + len(line4)) == 0)):
			printTime()
			print "Total arrivals for the day:", totalArrivals
			# print any other necessary data
			# End the loop
			break

		print "Total Arrivals", totalArrivals
		print "# of remaining customers:", (len(line1) + len(line2) + len(line3) + len(line4))


runSimulation()

'''
# Case 6 (Line switch):
		elif (getNextEvent() == ts and ts < tc):
			maxLineLength = max(len(line1), len(line2), len(line3), len(line4))

			# Set longest line
			if (maxLineSize == len(line1)):
				longestLine = line1
			elif (maxLineSize == len(line2)):
				longestLine = line2
			elif (maxLinesize == len(line3)):
				longestLine = line3
			else:
				longestLine = line4

	        lastInLineIndex = longestLine[maxLineSize - 1]   

	        # Makes a temporary copy of the longest line list
	        temp = list(longestLine)

	        # Remove last person from temp line
	        del temp[maxLineSize-1]       
	        
	        if(cmp(temp, getShortestLineSwitch(temp)) == False): 
	        	getSmallestLine().push(lastInLineIndex)
	       	
	        t = ts
	        ts = generateSwitchTime()'''