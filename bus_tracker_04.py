import time
import urllib
from xml.etree.ElementTree import parse

office_lat = 41.880262
office_lon = -87.668452

# What should I now?
# Reading direction from command line

def read_bus_data():
	u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	doc = parse(u)	
	return doc

def find_candidate(xml, direction = 'south'):
	candidates = []
	for bus in xml.findall('bus'):
		d = bus.findtext('d').lower()
		lat = float(bus.findtext('lat'))
		lon = float(bus.findtext('lon'))
		bid = bus.findtext('id')
		if lat > office_lat and d.startswith(direction):
			candidates.append({
				'busid' : bid,
				'lat' : lat,
				'lon' : lon ,
				'direction': d
				})
	return candidates

def find_nearest_candidates(candidates, distance_range = 0.5):
	# search into the given candidate busses and find those busses are closer then given distance
	pass

def monitor(candidates, alarm_distance):
	# Check is there any bus among give candidates that its distance to my location 
	# is less than alarm_distance? If yes then return that bus 
	return False

def display_candidates(candidates):
	#print cadidate BusId, LAT, Direction, Distance to my location
	pass

if __name__ == "__main__":
	import sys
	direction = sys.argv[1]

	xml = read_bus_data()

	candidates = find_candidate(xml, direction)

	print 'Candidates...'
	for c in candidates:
		print c['busid'], c['lat'], c['direction']
		print '-' * 50

	print 'DONE :)'


