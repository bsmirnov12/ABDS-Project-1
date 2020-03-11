# UT-TOR-DATA-PT-01-2020-U-C Team project #1
# (c) Boris Smirnov

# The module parces gml file with FED border coordinates, calculates centers of the FEDs
# Exports data into csv file with original coordinate system

import csv
import xml.etree.ElementTree as et

def find_center(pos_str):
 
    coords = pos_str.split()
    
    max_x, max_y = 0.0, 0.0
    min_x, min_y = 9999999.99999999, 9999999.99999999

    for i in range(0, len(coords), 2):
        coord_x = float(coords[i])
        coord_y = float(coords[i+1])
        
        if coord_x > max_x:
            max_x = coord_x
        elif coord_x < min_x:
            min_x = coord_x
        
        if coord_y > max_y:
            max_y = coord_y
        elif coord_y < min_y:
            min_y = coord_y

    avg_x = (max_x + min_x) / 2.0
    avg_y = (max_y + min_y) / 2.0
    return avg_x, avg_y

def province_en(str):
    return str.split(' / ')[0]

# Defining namespace prefixes for element names
gml = '{http://www.opengis.net/gml}'
fme = '{http://www.safe.com/gml/fme}'
ns = {
    'gml': 'http://www.opengis.net/gm',
    'fme': 'http://www.safe.com/gml/fme'
}

# Defining element names
FED      = f"{fme}lfed000a16g_e"
FED_ID   = f"{fme}FEDUID"
FED_NAME = f"{fme}FEDENAME"
PR_ID    = f"{fme}PRUID"
PR_NAME  = f"{fme}PRNAME"
POS_LIST = f"{gml}posList"

tree = et.parse('lfed000a16g_e.gml')
root = tree.getroot()

csv_fname = 'lfed000a16g_e.csv'

with open(csv_fname, 'w', newline='', encoding='utf-8') as csvfile: 

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write column headers
    csvwriter.writerow(['FED Id', 'FED Name', 'Province Id', 'Privince Name', 'x', 'y'])

    for district in root.iter(FED):
        fed_id   = int(district.find(FED_ID).text)
        fed_name = district.find(FED_NAME).text
        pr_id    = int(district.find(PR_ID).text)
        pr_name  = province_en(district.find(PR_NAME).text)
        pos_list = district.find(f".//{POS_LIST}")
        center_x, center_y = find_center(pos_list.text)
        print(fed_id, fed_name, pr_id, pr_name, center_x, center_y)
        csvwriter.writerow([fed_id, fed_name, pr_id, pr_name, "{:.8f}".format(center_x), "{:.8f}".format(center_x)])
