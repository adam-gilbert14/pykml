""" UTIL - a collection of utility methods that operate on KML documents"""
import re

def count_elements(doc):
    "Counts the number of times each element is used in a document"
    summary = {}
    for el in doc.iter():
        try:
            namespace, element_name = re.search('^{(.+)}(.+)$', el.tag).groups()
        except:
            namespace = None
            element_name = el.tag
        if not summary.has_key(namespace):
            summary[namespace] = {}
        if not summary[namespace].has_key(element_name):
            summary[namespace][element_name] = 1
        else:
            summary[namespace][element_name] += 1
    return summary

#def get_camera_location(lat1,lon1,altitude1,heading1,range1):
#    "Determines the Camera location given LookAt parameters"
#    
#    #ref: http://en.wikipedia.org/wiki/Mercator_projection
#    # N - Northing
#    # E - Easting
#    # lambda - longitude
#    # phi - latitude
#    # R - radius = 6378137m
#    
#    # TODO: implement
##    # spherical mercator equations
#     #E = R (lambda - lambda0)
#     #    N = R ln tan(pi / 4 + phi / 2)
##
##    # reverse spherical mercator
##    lambda = E / R + lambda0
##   phi - pi/2 - 2*arctan(exp(-N/R))
#    
#    return lat2,lon2,alt2

