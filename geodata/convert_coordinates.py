# UT-TOR-DATA-PT-01-2020-U-C Team project #1
# (c) Boris Smirnov

# The module reads csv file with NAD83 Statistics Canada Lambert coordinates
# and converts them into WGS 84 World Geodetic System 1984 (GPS) coordinates using epsg.io API
# For details see:
# https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
# https://epsg.io/3347
# https://epsg.io/4326
# API Reference: https://github.com/maptiler/epsg.io

import requests
import json
import csv
import time

# Coordinate system EPSG ids for coordinate transformation
NAD83 = 3347 # used at Stats Canada
WGS84 = 4326 # used with Google Maps

url=f"http://epsg.io/trans?s_srs={NAD83}&t_srs={WGS84}"

src_fname = 'lfed000a16g_e.csv'
dst_fname = 'geodata.csv'

src_file = open(src_fname, 'r', newline='', encoding='utf-8')
src_csv = csv.reader(src_file, delimiter=',')

territories = [60, 61, 62] # Yukon, NWT, Nunavut
territory_capital = [(60.7428612, -135.1366892), (62.4539497, -114.3743066), (63.7475018, -68.5106334)]

with open(dst_fname, 'w', newline='', encoding='utf-8') as dst_file:
    dst_csv = csv.writer(dst_file, delimiter=',')

    header = next(src_csv) # skip source header

    # Write header
    # Latitude is y coordinate (vertical, N), Longitude is x coordinate (horizontal, E)
    dst_csv.writerow(['FED Id', 'FED Name', 'Province Id', 'Privince Name', 'Latitude', 'Longitude'])

    for row in src_csv:

        prov_id = int(row[2])
        if prov_id in territories:
            idx = prov_id - 60
            lat, lon = territory_capital[idx]
            dst_csv.writerow(row[0:4] + [lat, lon])
            continue

        coord_x = row[4]
        coord_y = row[5]

        pause = 10 # seconds
        print("Query #{:03d}: {:d} sec pause ".format(src_csv.line_num - 1, pause), end='', flush=True)
        for i in range(pause): time.sleep(1); print(".", end='', flush=True)
        print(" go!", flush=True)
                                                                
        query = url + f"&x={coord_x}&y={coord_y}"
        new_coords = requests.get(query).json()

        dst_csv.writerow(row[0:4] + [new_coords['y'], new_coords['x']])

# done