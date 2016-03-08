import math
import random
import support
import SingleServer
 
# Random variable library for generating random variables
import numpy

# Global Variables:
float t
float ta, td1, td2, td3, td4
float tc

# State Variables
int n1, n2, n3, n4

# Total number of customer arrivals throughout the day
int totalArrivals

# Generates arrival time, along with number of items in cart
def generateArrivalTime(lam):
	# Non-homogenous Poisson distribution
	ta = numpy.random.poisson(lam, 10000)
	totalArrivals += 1

#Parker
def generateDepartureTime():
	# If customer is at the front of the line -> generate departure time using weibull dist.

def updateTime(eventTime):
	# Adds event time to current time
	t += eventTime

def getTime():
	return t

#Parker
def getItemsInCart(line):
	# Return number of items in customer's cart in a given line

#Jack
def generateItemsInCart():

#Sai
def chooseLine():

#Eric
def getEstimatedLineSize():


# Main loop
def runSimulation():
	while (True):
		# Case 1:
		if ((ta <= min(td1, td2, td3, td4)) and (ta < tc)):

			updateTime(ta)
			generateItemsInCart()
			chooseLine()
			# Increment total arrivals by 1
			totalArrivals += 1
			# Increment number of customers in line chosen by customer
			n1 += 1
			generateArrivalTime()j






		
