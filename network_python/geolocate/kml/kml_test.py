#!/usr/bin/python

import simplekml

cities = [
    ('Aberdeen, Scotland', '1.2.3.4', 57.15, -2.15),
    ('Adelaide, Australia', '2.3.4.5', -34.916667, 138.6),
    ('Algiers, Algeria', '3.4.5.6', 36.833333, 3),
    ('Zurich, Switzerland', '4.5.6.7', 47.35, 8.516667)
]


# Create an instance of Kml
kml = simplekml.Kml(open=1)

style = simplekml.Style()
style.labelstyle.color = simplekml.Color.red  # Make the text red
style.labelstyle.scale = 4  # Make the text twice as big
style.iconstyle.scale = 3  # Icon thrice as big
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/purple-stars.png' #'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

# Create a point named "The World" attached to the KML document with its coordinate at 0 degrees latitude and longitude.
# All the point's properties are given when it is constructed.
single_point = kml.newpoint(name="The World", coords=[(0.0,0.0)])

# Create a point for each city. The points' properties are assigned after the point is created
for city, ip, lat, lon in cities:
    pnt = kml.newpoint()
    pnt.name = city
    pnt.description = "{0}".format(ip)
    pnt.coords = [(lon, lat)]
    pnt.style = style

# Save the KML
kml.save("test.kml")