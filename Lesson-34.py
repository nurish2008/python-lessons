# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:02:15 2021

@author: Lesson-34
"""

import json
#import googlemaps

from apikey import APIKEY 

gmaps = googlemaps.Client(key=APIKEY)
data = gmaps.geocode('Olmazor','Toshkent','Uzbekistan')

g = json.dumps(data[0], indent = 4, sort_keys=True)
print(g)
