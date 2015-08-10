import time
import urllib
from xml.etree.ElementTree import parse

office_lat = 41.880262
office_lon = -87.668452

# What should I now?
# Calculate distance between 2 points based on their latitude Delta LAT * 69.047
# Then find all Buses coming to you and close enough for you to be notofied
# Create display function for candidates

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


def calculate_distance (l1, l2):
	return 69.047 * abs(l1 - l2)

def find_nearest_candidates(candidates, distance_range = 0.5):
	results = []
	for bus in candidates:
		dis = calculate_distance(bus['lat'], office_lat)
		if dis < distance_range:
			results.append( bus )
	return results

def monitor():
	return False

def display_candidates(candidates):
	for c in candidates:
		print c['busid'], c['lat'], c['direction'], calculate_distance(office_lat, c['lat'])

if __name__ == "__main__":
	import sys
	direction = sys.argv[1]
	distance = float(sys.argv[2])

	xml = read_bus_data()

	candidates = find_candidate(xml, direction)

	print 'Candidates...'
	display_candidates(candidates)

	print '='*50
	
	nearest_candidates = find_nearest_candidates(candidates, distance)

	print 'Nearest...'
	display_candidates(nearest_candidates)

	print 'DONE :)'


