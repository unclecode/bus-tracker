import time
import urllib
from xml.etree.ElementTree import parse

office_lat = 41.880262
office_lon = -87.668452

# What should I now?
# We will show the first hot buss on google map using google map url api

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
		dis = calculate_distance(bus['lat'] , office_lat)
		if dis < distance_range:
			results.append( bus )
	return results

def monitor(direction, alarm_distnce):
	print 'Monitoring....'
	xml = read_bus_data()
	candidates = find_candidate(xml, direction)

	print 'Candidates...'
	display_candidates(candidates)

	hot_busses = find_nearest_candidates(candidates, alarm_distnce)
	
	if hot_busses != []:
		return hot_busses
	return {}

def display_candidates(candidates):
	for c in candidates:
		print c['busid'], c['lat'], c['direction'], calculate_distance(office_lat, c['lat'])

if __name__ == "__main__":
	import sys
	direction = sys.argv[1]
	distance = float(sys.argv[2])

	while True:
		hot_busses = monitor(direction, distance)
		if hot_busses:
			import webbrowser
			print 'FOUND :) ... '
			display_candidates(hot_busses)

			webbrowser.open('https://www.google.com/maps?q=%f,%f' % (hot_busses[0]['lat'], hot_busses[0]['lon']))	
			break;	
		print '=' * 50
	print 'DONE :)'


