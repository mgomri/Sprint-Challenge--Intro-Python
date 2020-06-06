import csv
#Make a class City that has fields name lat lon

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  
  def __str__(self):
    return f'{self.__class__.__name__}("{self.name}", {self.lat}, {self.lon})'
  

# Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the 
# `cities` list

cities = []
def cityreader(cities=[]):
  with open('./src/cityreader/cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print('\n')
    for row in csv_reader:
      if line_count == 0:
        pass
      else:
        city = City(row[0], row[3], row[4])
        cities.append(city)
      line_count += 1 
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.

for c in cities:
  print(c)
print('\n')


#_________________________________________________________________________________________
#                                        Stretch
#_________________________________________________________________________________________

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  within = []
  for city in cities:
    if float(city.lat) > min(lat1, lat2) and float(city.lat) < max(lat1, lat2):
      if float(city.lon) > min(lon1, lon2) and float(city.lon) < max (lon1, lon2):
        within.append(city)
  return within

coordinates1 = input('enter lat1, lon1:').split(',')
coordinates2 = input('enter lat2, lon2:').split(',')
lat1 = float(coordinates1[0])
lon1 = float(coordinates1[1])
lat2 = float(coordinates2[0])
lon2 = float(coordinates2[1])

within = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
print('\n')
for w in within:
  print(f'{w.name}: ({w.lat}, {w.lon})')
  


 
