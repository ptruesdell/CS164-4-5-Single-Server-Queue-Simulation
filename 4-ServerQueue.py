import math
import random
 
# Random variable library for generating random variables
#import numpy

a_jillion = 100000.0
a_kajillion = 10.0 * a_jillion


# Current time variable
t = 0.0

# Time of line switch
ts = a_jillion

switch = 0

ta = 0.0

# Departure times for 4-server
td1 = a_jillion
td2 = a_jillion
td3 = a_jillion
td4 = a_jillion

# Closing time variable
tc = 100.0

# Initialize line lists
# Line lists will contain customers represented by an integer number of items in cart
line1 = list()
line2 = list()
line3 = list()
line4 = list()

longLineSize = 1

# Total number of customer arrivals throughout the day
totalArrivals = 0

# Initialize r.v. generation parameters

# Arrival time parameter
lam = 0.5

# Departure time parameters
alpha = 0.5
beta = 4.0

# Cart size parameter
cartSizeLam = 0.5

switchLam = 0.5

# Logging variables for analysis
maxLineLengthLogger = 0

# Generates arrival time, along with number of items in cart
def generateArrivalTime():
	global t
	# Non-homogenous Poisson distribution
	# random variable u
	u = random.random()
	# Set New Arrival time to exponential equation
	Y = (-lam) * math.log(1.0 - u)
	return Y + t


# TODO: change to weibull
def generateDepartureTime():
	global t, beta, alpha
	Y = beta * math.exp((1.0/alpha) * math.log(-math.log(alpha)))
	return Y + t

# Exponential
def generateSwitchTime():
	global t
	u = random.random()
	Y = (-switchLam) * math.log(1 - u)
	return Y + t

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
	sum = 0.0
	for i in range(len(line)):
		sum += line[i]
	return sum + (5.0 * len(line))

# Returns shortest estimated line
# Return value is the line that the customer chooses
def chooseLine():

	global line1, line2, line3, line4

	if min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line1):
		return 1
	elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line2):
		return 2
	elif min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4)) == getEstimatedWaitTime(line3):
		return 3
	else:
		return 4

def getNextEvent():
	global ta, td1, td2, td3, td4, ts
	return min(ta, td1, td2, td3, td4, ts)

def printNextEvent():
	global ta, td1, td2, td3, td4, ts
	if (getNextEvent() == ta):
		print "Next event is an ARRIVAL at:", ta
	elif (getNextEvent() == td1):
		print "Next event is a DEPARTURE from line 1 at:", td1
	elif (getNextEvent() == td2):
		print "Next event is a DEPARTURE from line 2 at:", td2
	elif (getNextEvent() == td3):
		print "Next event is a DEPARTURE from line 3 at:", td3
	elif (getNextEvent() == td4):
		print "Next event is a DEPARTURE from line 4 at:", td4
	elif (getNextEvent() == ts):
		print "Next event is a lane SWITCH at:", ts


def getLongestLine():

	global line1, line2, line3, line4
	return max(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4))

def getShortestLineSwitch():

	global line1, line2, line3, line4

	short = min(getEstimatedWaitTime(line1), getEstimatedWaitTime(line2), getEstimatedWaitTime(line3), getEstimatedWaitTime(line4))
	if (short == getEstimatedWaitTime(line1)):
		return line1
	elif (short == getEstimatedWaitTime(line2)):
		return line2
	elif (short == getEstimatedWaitTime(line3)):
		return line3
	elif (short == getEstimatedWaitTime(line4)):
		return line4

def printTime():
	global t
	print "Current time:", t

def printNumCustomersInLine():
	global line1, line2, line3, line4
	print "------------------------------"
	print "# of customers in line 1:", len(line1)
	print "# of customers in line 2:", len(line2)
	print "# of customers in line 3:", len(line3)
	print "# of customers in line 4:", len(line4)
	print "------------------------------"

def printDepartureTimes():
	if (td1 < a_jillion):
		print "Line 1 Departure Time:", td1
	if (td2 < a_jillion):
		print "Line 2 Departure Time:", td2
	if (td3 < a_jillion):
		print "Line 3 Departure Time:", td3
	if (td4 < a_jillion):
		print "Line 4 Departure Time:", td4

# Main loop
def runSimulation():

	global t, ta, td1, td2, td3, td4, ts, tc
	global line1, line2, line3, line4
	global totalArrivals, lam, cartSizeLam
	global maxLineLengthLogger
	global switch

	ts = generateSwitchTime()

	# Initialize first arrival time
	ta = generateArrivalTime()

	while (getNextEvent() < tc):

		printTime()
		printNextEvent()

		# Case 1 (Arrival occurs before departure from any line and before closing):
		if (getNextEvent() == ta and ta < tc):

			# Update current time by time of arrival
			t = ta

			# Increment total arrivals by 1
			totalArrivals += 1

			# Add customer to "shortest" line
			items = generateItemsInCart()
			if (chooseLine() == 1):
				line1.append(items)
				if (len(line1) == 1):
					td1 = generateDepartureTime()
			elif (chooseLine() == 2):
				line2.append(items)
				if (len(line2) == 1):
					td2 = generateDepartureTime()
			elif (chooseLine() == 3):
				line3.append(items)
				if (len(line3) == 1):
					td3 = generateDepartureTime()
			elif (chooseLine() == 4):
				line4.append(items)
				if (len(line4) == 1):
					td4 = generateDepartureTime()

			printNumCustomersInLine()

			# Generate and set new arrival time
			ta = generateArrivalTime()
			t = getNextEvent()

		# Case 2 (Departure from line 1):
		elif (getNextEvent() == td1 and td1 < tc):

			# Update current time by earliest departure time
			t = td1

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

			# Remove departed customer from line with earliest departure time
			line4.pop(0)

			printNumCustomersInLine()

			if (len(line4) > 0):
				td4 = generateDepartureTime()
			else: 
				td4 = a_jillion

		elif (getNextEvent() == ts and ts < tc):
		    # Update time
		    t = ts
    		# Generate next switch time
   		    ts = generateSwitchTime()

   		    # The max line must be greater than 1 to switch
		    if ((max(len(line1), len(line2), len(line3), len(line4))) > 1):

				# Make temporary line of longest line and find the items of last person
				if (getLongestLine() == getEstimatedWaitTime(line1)):
				    lastInLineIndex = line1[len(line1) - 1]	# Get last person's items
				    line1.pop()								# Remove them from the line
				    print "Line 1 is the longest"
				    longestLine = list(line1)				# Copy the line
				    previousLine = 1						# Save line number for later to reinsert them in line if not beneficial
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line2)):
				    lastInLineIndex = line2[len(line2) - 1]
				    line2.pop()
				    print "Line 2 is the longest"
				    longestLine = list(line2)
				    previousLine = 2
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line3)):
				    lastInLineIndex = line3[len(line3) - 1]
				    line3.pop()		
				    print "Line 3 is the longest"	   
				    longestLine = list(line3)
				    previousLine = 3
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line4)):
				    lastInLineIndex = line4[len(line4) - 1]
				    line4.pop()
				    print "Line 4 is the longest"
				    longestLine = list(line4)
				    previousLine = 4
				    print getEstimatedWaitTime(longestLine)

				if (longestLine != getShortestLineSwitch()):		#if (longest line without last person) is NOT (the shortest line)

					if (len(getShortestLineSwitch()) == 0):				#and there is nobody in the new line

						if(len(line1) == 0):	#Generate new departure time for new line		     
							td1 = generateDepartureTime()
							line1.append(lastInLineIndex)
						elif(len(line2) == 0):
							td2 = generateDepartureTime() 
							line2.append(lastInLineIndex)
						elif(len(line3) == 0):
							td3 = generateDepartureTime()
							line3.append(lastInLineIndex)
						elif(len(line4) == 0):
							td4 = generateDepartureTime()
							line4.append(lastInLineIndex)

					elif(line1 == getShortestLineSwitch()):

						line1.append(lastInLineIndex)

					elif(line2 == getShortestLineSwitch()):

						line2.append(lastInLineIndex)

					elif(line3 == getShortestLineSwitch()):

						line3.append(lastInLineIndex)

					elif(line4 == getShortestLineSwitch()):

						line4.append(lastInLineIndex)

				else: # If switching lines would not be beneficial (shortest line is theirs without them)
				
				    if (previousLine == 1):			#if they came from line 1
						line1.append(lastInLineIndex)		#put them back in line
				    elif (previousLine == 2):
						line2.append(lastInLineIndex)
				    elif (previousLine == 3):
						line3.append(lastInLineIndex)
				    elif (previousLine == 4):
						line4.append(lastInLineIndex)

		print "------------------------------"
		print "Line 1:", line1
		print "Line 2:", line2
		print "Line 3:", line3
		print "Line 4:", line4
		print "------------------------------"

		# Keeps track of the longest line size throughout the simulation
		if (max(len(line1), len(line2), len(line3), len(line4)) > maxLineLengthLogger):
			maxLineLengthLogger = max(len(line1), len(line2), len(line3), len(line4))

	# Keep new arrivals from occuring after closing time
	ta = a_jillion

	# Case 7 (Next departure happens after closing and at least one customer is still in line)
	# Loop runs only past closing time when there are customers still in line
	while (len(line1) + len(line2) + len(line3) + len(line4) > 0):

		printTime()
		printNextEvent()

		if (getNextEvent() == td1 and len(line1) >= 1):
			t = td1
			line1.pop(0)
			printNumCustomersInLine()
			if (len(line1) > 0):
				td1 = generateDepartureTime()
			else:
				td1 = a_jillion
			
		elif (getNextEvent() == td2 and len(line2) >= 1):
			t = td2
			line2.pop(0)
			printNumCustomersInLine()
			if (len(line2) > 0):
				td2 = generateDepartureTime()
			else:
				td2 = a_jillion

		elif (getNextEvent() == td3 and len(line3) >= 1):
			t = td3
			line3.pop(0)
			print printNumCustomersInLine()
			if (len(line3) > 0):
				td3 = generateDepartureTime()
				t = td3
			else:
				td3 = a_jillion

		elif (getNextEvent() == td4 and len(line4) >= 1):
			t = td4
			line4.pop(0)
			print printNumCustomersInLine()
			if (len(line4) > 0):
				td4 = generateDepartureTime()
			else:
				td4 = a_jillion

		elif (getNextEvent() == ts):

		    # Update time
		    t = ts
    		# Generate next switch time
   		    ts = generateSwitchTime()

   		    # The max line must be greater than 1 to switch
		    if ((max(len(line1), len(line2), len(line3), len(line4))) > 1):

				# Make temporary line of longest line and find the items of last person
				if (getLongestLine() == getEstimatedWaitTime(line1)):
				    lastInLineIndex = line1[len(line1) - 1]	# Get last person's items
				    line1.pop()								# Remove them from the line
				    print "Line 1 is the longest"
				    longestLine = list(line1)				# Copy the line
				    previousLine = 1						# Save line number for later to reinsert them in line if not beneficial
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line2)):
				    lastInLineIndex = line2[len(line2) - 1]
				    line2.pop()
				    print "Line 2 is the longest"
				    longestLine = list(line2)
				    previousLine = 2
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line3)):
				    lastInLineIndex = line3[len(line3) - 1]
				    line3.pop()		
				    print "Line 3 is the longest"	   
				    longestLine = list(line3)
				    previousLine = 3
				    print getEstimatedWaitTime(longestLine)
				elif (getLongestLine() == getEstimatedWaitTime(line4)):
				    lastInLineIndex = line4[len(line4) - 1]
				    line4.pop()
				    print "Line 4 is the longest"
				    longestLine = list(line4)
				    previousLine = 4
				    print getEstimatedWaitTime(longestLine)

				if (longestLine != getShortestLineSwitch()):		#if (longest line without last person) is NOT (the shortest line)

					if (len(getShortestLineSwitch()) == 0):			#and there is nobody in the new line

						if(len(line1) == 0):						#Generate new departure time for new line		     
							td1 = generateDepartureTime()
							line1.append(lastInLineIndex)
						elif(len(line2) == 0):
							td2 = generateDepartureTime() 
							line2.append(lastInLineIndex)
						elif(len(line3) == 0):
							td3 = generateDepartureTime()
							line3.append(lastInLineIndex)
						elif(len(line4) == 0):
							td4 = generateDepartureTime()
							line4.append(lastInLineIndex)

					elif(line1 == getShortestLineSwitch()):

						line1.append(lastInLineIndex)

					elif(line2 == getShortestLineSwitch()):

						line2.append(lastInLineIndex)

					elif(line3 == getShortestLineSwitch()):

						line3.append(lastInLineIndex)

					elif(line4 == getShortestLineSwitch()):

						line4.append(lastInLineIndex)

				else: # If switching lines would not be beneficial (shortest line is theirs without them)
				
				    if (previousLine == 1):			#if they came from line 1
						line1.append(lastInLineIndex)		#put them back in line
				    elif (previousLine == 2):
						line2.append(lastInLineIndex)
				    elif (previousLine == 3):
						line3.append(lastInLineIndex)
				    elif (previousLine == 4):
						line4.append(lastInLineIndex)

		# Log arrivals/remaining
		printTime()
		print "Total Arrivals", totalArrivals
		print "------------------------------"
		print "Line 1:", line1
		print "Line 2:", line2
		print "Line 3:", line3
		print "Line 4:", line4
		print "------------------------------"

	# Log time, total arrivals, and # customers remaining at end of simulation
	printTime()
	print "Total arrivals for the day:", totalArrivals
	print "# of remaining customers:", (len(line1) + len(line2) + len(line3) + len(line4))
	print "Longest line length:", maxLineLengthLogger

runSimulation()