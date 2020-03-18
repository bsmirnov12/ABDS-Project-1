# UT-TOR-DATA-PT-01-2020-U-C Team project #1
# (c) Boris Smirnov

# The module reads geodata.csv file with FED GPS coordinates,
# and for each province calculates middle point based on those coordinates.
# Then, it creates provinces.csv containing province id, name, and latitude-longitude pair.
# The file then can be used for putting markers on provinces using GMaps API

import csv

src_fname = 'geodata.csv'
dst_fname = 'provinces.csv'

province_ids = []
province_db = { 0: { 'name': "", 'max_lat': 0.0, 'min_lat': 0.0, 'max_lon': 0.0, 'min_lon': 0.0 } }

# fix centers of the territories
territories = [60, 61, 62] # Yukon, NWT, Nunavut
territory_center = [(63.6025218,-135.9292136), (63.608103, -118.799387), (64.31758800, -96.02247400)]

# read source file with coordinates
src_file = open(src_fname, 'r', newline='', encoding='utf-8')
src_csv = csv.reader(src_file, delimiter=',')

header = next(src_csv) # skip source header

for row in src_csv:

    prov_id = int(row[2])
    prov_name = row[3]
    lat = float(row[4])
    lon = float(row[5])

    if not prov_id in province_ids:
        # create database record for the province
        province_ids.append(prov_id)
        province_db[prov_id] = {
            'name': prov_name, 
            'max_lat': lat, 'min_lat': lat, 'max_lon': lon, 'min_lon': lon
        }
    else:
        # update database record fot the province
        if lat > province_db[prov_id]['max_lat']:
            province_db[prov_id]['max_lat'] = lat
        elif lat < province_db[prov_id]['min_lat']:
            province_db[prov_id]['min_lat'] = lat
        
        if lon > province_db[prov_id]['max_lon']:
            province_db[prov_id]['max_lon'] = lon
        elif lon < province_db[prov_id]['min_lon']:
            province_db[prov_id]['min_lon'] = lon

# write output file
with open(dst_fname, 'w', newline='', encoding='utf-8') as dst_file:
    dst_csv = csv.writer(dst_file, delimiter=',')

    # Write header
    # Latitude is y coordinate (vertical, N), Longitude is x coordinate (horizontal, E)
    dst_csv.writerow(['Province Id', 'Province Name', 'Latitude', 'Longitude'])

    # calculate middle points for each province and write them to the file
    province_ids = sorted(province_ids)
    for pid in province_ids:
        if pid in territories:
            idx = pid - 60
            avg_lat, avg_lon = territory_center[idx]
        else:
            avg_lat = (province_db[pid]['max_lat'] + province_db[pid]['min_lat']) / 2
            avg_lon = (province_db[pid]['max_lon'] + province_db[pid]['min_lon']) / 2
        dst_csv.writerow([str(pid), province_db[pid]['name'], "{:.8f}".format(avg_lat), "{:.8f}".format(avg_lon)])

