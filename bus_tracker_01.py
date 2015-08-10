office_lat = 41.880262
office_lon = -87.668452


def read_bus_data():
	# Read all busses location data from API and return a XML handler
	pass

def find_candidate(xml, direction = 'south'):
	# Extract all busses information (BusId, LAT, Direction) of those busses are heading to
	# the given direction and also they will cross my location
	pass

def find_nearest_candidates(candidates, distance_range = 0.5):
	# search into the given candidate busses and find those busses are closer then given distance
	pass

def monitor(candidates, alarm_distance):
	# Check is there any bus among give candidates that its distance to my location 
	# is less than alarm_distance? If yes then return that bus 

	return False

def display_candidates(candidates):
	#print cadidate BusId, LAT, Direction, Distance to my location

print 'DONE :)'


