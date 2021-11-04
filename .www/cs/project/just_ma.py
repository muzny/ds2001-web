#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

"""
Felix Muzny
DS 2001 - map examples

Example of using shape files from cartopy, with only massachusetts

See various shape files available through this interface:
    https://scitools.org.uk/cartopy/docs/v0.18/tutorials/using_the_shapereader.html
    
    
List of shapefiles available from natural earth:
    https://www.naturalearthdata.com/downloads/
    https://www.naturalearthdata.com/downloads/10m-cultural-vectors/
    
"""


def main():    
    ax = plt.axes([0, 0, 1, 1],
                  projection=ccrs.LambertConformal())

    ax.set_extent([-100, -70, 40, 45], ccrs.Geodetic())

    shapename = 'admin_1_states_provinces_lakes_shp'
    states_shp = shpreader.natural_earth(resolution='110m',
                                         category='cultural', 
                                         name=shapename)

    plt.title('Massachusetts')
    
    states = shpreader.Reader(states_shp)
    
    
    # just look for MA
    for state in states.records():
        if state.attributes['name'] == "Massachusetts":
            print(state)
            facecolor = 'yellow'
            edgecolor = 'black'
            print(state.geometry)
            ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                              facecolor=facecolor, edgecolor=edgecolor)


    # add latitude and longitude lines
    ax.gridlines(draw_labels=True)
    plt.show()

if __name__ == '__main__':
    main()