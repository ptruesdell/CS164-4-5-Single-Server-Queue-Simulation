import math #math library
import random
 
# Random variable library for generating random variables
import numpy

# Global Variables:
float t
float ta, td
float tc

# Total number of customer arrivals throughout the day
int totalArrivals

# Generates arrival time, along with number of items in cart
def generateArrival(lam):
	# Non-homogenous Poisson distribution
	ta = numpy.random.poisson(lam, 10000)


def generateDepartureTime():
	# If customer is at the front of the line -> generate departure time using weibull dist.

def updateTime(eventTime):
	# Adds event time to current time
	t += eventTime

def getTime():
	return t

def getItemsInCart(line):
	# Return number of items in customer's cart in a given line

# Main loop
def runSimulation():
	while (True):
		
