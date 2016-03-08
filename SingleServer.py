import random
import math

# Global Variables
t = 0
	n_a = 0
	n_d = 0
	state = 0

	arrivalRate = .5
	departureRate = .5

	#First arrival time
	u = random.random()
	ta = (-arrivalRate)*math.log(1 - u)

	#time of departure set to "infinity"
	td = 10000

	closingTime = 10

	#lists that hold times for arrivals and departures
	arrivals = []
	departures = []

def singleServerSimulation():

	print("Time : state")

	while(True):
		# CASE 1
		if((t_a <= td) and (t_a <= closingTime)):
			#update time
			t = t_a

			#update state
			state = state + 1

			#update next time of arrival
			u = random.random()
			t_a = t + (-arrivalRate)*math.log(1 - u)

			#check state
			if(state == 1):
				#update time of next departure
				u = random.random()
				y = (-departureRate)*math.log(1 - u)
				td = t + y

			print(str(t) + ' : ' + str(state))
			
			#collect data
			arrivals.append(t)

		# CASE 2
		#departure is next event and not closing time yet
		elif((td <= t_a) and (td <= closingTime)):
			#update time
			t = td

			#update state
			state = state - 1

			#update number of departures
			n_d = n_d + 1

			#check state
			if(state == 0):
				#update next time of departure
				td = 10000
			else:
				#update next time of departure
				u = random.random()
				y = (-departureRate)*math.log(1 - u)
				td = t + y
			
			print(str(t) + ' : ' + str(state))

			#collect data
			departures.append(t)

		# CASE 3
		#next event is after closing time with people left in line
		elif((min(t_a, td) > closingTime) and (state > 0)):
			#update time
			t = td

			#update state
			state = state - 1

			#update number of departures
			n_d = n_d + 1

			#check state
			if(state > 0):
				#update next departure
				u = random.random()
				y = (-departureRate)*math.log(1 - u)
				td = t + y

			print(str(t) + ' : ' + str(state))

			#collect data
			departures.append(t)

		# CASE 4
		elif((min(t_a, td) > closingTime) and (state == 0)):
			#collect output data
			tp = max(t - closingTime, 0)
			break


	print("# Arrivals: " + str(len(arrivals)))
#	print("Arrival times: " + str(arrivals))
#	print("Departure times: " + str(departures))
	print("tp: " + str(tp))

singleServerSimulation()
