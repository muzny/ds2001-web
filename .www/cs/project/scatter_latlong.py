#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
DS 2001 - map examples

Example of turning latitude and longitude
coordinates into a graph (with no outlines).

If you have sufficient data points, a scatter plot will
show the geographic layout of your data. if you don't have suffifient
data, then it will appear like random points.
"""

#https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html


import matplotlib.pyplot as plt


# Latitudes and longitudes of the middles of all fifty states
# downloaded from:
# https://www.latlong.net/category/states-236-14.html


LATITUDES = [44.5,
39,
44,
31,
44.5,
41.700001,
44,
43,
44,
41.5,
38.5,
33,
40,
39,
41.599998,
34.799999,
40.273502,
38.573936,
27.994402,
39.876019,
45.367584,
44.182205,
33.247875,
19.741755,
66.160507,
35.860119,
37.926868,
39.833851,
37.839333,
47.650589,
46.39241,
36.084621,
46.96526,
47.751076,
39.41922,
39.113014,
40.367474,
32.31823,
42.032974,
34.307144,
33.836082,
41.203323,
34.048927,
39.045753,
42.407211,
36.778259,
44.068203,
43.07597,
35.782169,
30.39183]

LONGITUDES = [-89.5,
-80.5,
-72.699997,
-100,
-100,
-71.5,
-120.5,
-75,
-71.5,
-100,
-98,
-90,
-89,
-75.5,
-72.699997,
-92.199997,
-86.126976,
-92.60376,
-81.760254,
-117.224121,
-68.972168,
-84.506836,
-83.441162,
-155.844437,
-153.369141,
-86.660156,
-78.024902,
-74.871826,
-84.27002,
-100.437012,
-94.63623,
-96.921387,
-109.533691,
-120.740135,
-111.950684,
-105.358887,
-82.996216,
-86.902298,
-93.581543,
-106.018066,
-81.163727,
-77.194527,
-111.093735,
-76.641273,
-71.382439,
-119.417931,
-114.742043,
-107.290283,
-80.793457,
-92.329102]

if __name__ == "__main__":
    plt.scatter(LONGITUDES, 
                LATITUDES)
    # use color bars to color the points different ways
    
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Coordinates of the US")
    
    # example of saving a figure
    plt.savefig("myexcellentgraph.pdf",
                bbox_inches = "tight")
    
    plt.show()