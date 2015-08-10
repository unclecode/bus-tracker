import time
import urllib
from xml.etree.ElementTree import parse

office_lat = 41.880262
office_lon = -87.668452

# What should I now?
# http://ctabustracker.com/
# XML
# http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22
# How to read XML file in python

def read_bus_data():
	u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
	doc = parse(u)	
	return doc

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
	pass


xml = read_bus_data()

for bus in xml.findall('bus'):
	d = bus.findtext('d')
	lat = float(bus.findtext('lat'))
	bid = bus.findtext('id')
	print bid, d, lat

print '----------- Buses on my north---------'
for bus in xml.findall('bus'):
	d = bus.findtext('d')
	lat = float(bus.findtext('lat'))
	bid = bus.findtext('id')
	if lat > office_lat:
		print bid, d, lat

print 'DONE :)'


