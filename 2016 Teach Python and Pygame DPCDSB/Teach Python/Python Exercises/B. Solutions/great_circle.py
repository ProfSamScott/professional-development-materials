"""Solution to the great circle exercise

Sam Scott, January 19, 2016"""

import math

# CONSTANTS
EARTH_RADIUS = 6371.01

# INPUT
lat1 = math.radians(float(input("Enter Point 1 Latitude:  ")))
lon1 = math.radians(float(input("Enter Point 1 Longitude: ")))
lat2 = math.radians(float(input("Enter Point 1 Latitude:  ")))
lon2 = math.radians(float(input("Enter Point 1 Longitude: ")))

# PROCESSING
d = EARTH_RADIUS * math.acos(
    math.sin(lat1) * math.sin(lat2) + 
    math.cos(lat1) * math.cos(lat2) * math.cos(lon1-lon2)
)

#OUTPUT
print("The distance between the points is: ",round(d,3),"km")
