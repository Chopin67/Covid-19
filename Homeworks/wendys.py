# azh5kn Alexandra Hickman av2jf Amara Vo
# could not finish
import math
import urllib.request
key = urllib.request.urlopen(' http://cs1110.cs.virginia.edu/files/wendys.csv')
text = key.read().decode('utf-8')
lines = text.split('\n')
line = []
row = []
for ch in lines:
   line.append(ch)
#print(line)

for x in line:
    row.append(x)
#print(row)
empty = []
for each in row:
    comma = each.find(',')
    latitude = (each[0:comma])
    empty.append(latitude)
for st in empty:
    flt = float(st)
    latitude = flt
print(empty)

#row  = line.split(',')
for number in line:
    latitude = line[:9]

def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees

    return dist
#given_latitude = input('Enter a latitude: ')
#given_longitude = input('Enter a longitude: ')
