import os
import pprint
from datetime import datetime 



os.chdir('/Users/sundarsritharan/Python/hf_python/advanced')
with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)


def convert2ampm(time24:str) -> str:
    """ convert 24 hrs time to Am/PM """ 
    return datetime.strptime(time24,'%H:%M').strftime('%I:%M%p')

flights2 = {}

for k,v in flights.items():
   flights2[convert2ampm(k)] = v.title()

print('--')
pprint.pprint(flights2)
print('--')

flight_times = []
for flight_time in flights.keys():
    flight_times.append(convert2ampm(flight_time))

destinations = []
for destination in flights.values():
    destinations.append(destination.title())

print(flight_times)
print(destinations)

print('--- lists comprehensed ---')

flight_times = [ convert2ampm(flight_time) for flight_time in flights.keys()]
destinations = [ destination.title() for destination in flights.values()]

print(flight_times)
print(destinations)

unique_destinations = set(flights2.values())
print(unique_destinations)

flight_times = [ k for k,v in flights2.items() if v == 'West End']

print(flight_times)

# list times for all destinations 
for dest in set(flights2.values()):
    print(dest, '->', [ k for k,v in flights2.items() if v == dest])

# list times for all destinations
when = {}
for dest in set(flights2.values()):
    when[dest] = [ k for k,v in flights2.items() if v == dest]

pprint.pprint(when)

#enhancing list of destination flight times
when2 = { dest: [ k for k,v in flights2.items() if v == dest] for dest in set(flights2.values())}

pprint.pprint(when2)