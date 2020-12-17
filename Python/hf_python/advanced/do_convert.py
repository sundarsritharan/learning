from datetime import datetime
import pprint 


def convert2ampm(time24:str) -> str:
    """ convert 24 hrs time to Am/PM """ 
    return datetime.strptime(time24,'%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

# dictionary comprehension 
fts = { convert2ampm(k):v.title() for k,v in flights.items()}

pprint.pprint(fts)
print()

# list of destination flight times
when = { dest: [ k for k,v in fts.items() if v == dest] for dest in set(fts.values())}

pprint.pprint(when)
print()