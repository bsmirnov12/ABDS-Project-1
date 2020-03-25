# Geodata information

## The goal

To determine central coordinates of Federal Electoral Districts (FED) suitable for quering Google Maps APIs.

The result is saved in geodata.csv

## Data Sources

### Statistics Canada

[Federal Electoral District Boundary Files](https://www150.statcan.gc.ca/n1/en/catalogue/92-171-X)

In the data request form choose:

* Format: Geography Markup Language (.gml)

* Boundary files: `[Federal electoral districts (2013 Representation Order), Digital Boundary File]`

Pressing **Continue** button should lead to [lfed000a16g_e.zip](http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lfed000a16g_e.zip)
	
The geographic coordinates data is proveded in GML (a flavour of XML) format.
The coordinates are represented as Lambert conformal conic projection (North American Datum of 1983 (NAD83))

The boundary file contains following information:
* FED id
* FED name in English and French (separately)
* Province id
* Province name in English and French (in one string)
* A list of coordinates that defines a bound around an FED

### ESPG registry

The registry of different coordinate systems.
This registry was accessed via 3rd party website [espg.io](https://epsg.io/) which provides coordinate system lookup and conversion service.

API for coordinate system transormation is described [here](https://github.com/maptiler/epsg.io)

ESPG code used for NAD83 Statistics Canada Lambert is [3347](https://epsg.io/3347).
ESPG code used for WGS 84 World Geodetic System 1984, used in GPS [4326](https://epsg.io/4326).


### Additional reading

https://en.wikipedia.org/wiki/Geography_Markup_Language

https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset

### Data Files

* lfed000a16g_e.gml - GML (XML) Data with FED and coordinates
* lfed000a16g_e.xsd - XML-schema for validation of lfed000a16g_e.gml
* 92-160-g2016002-eng.pdf, federal_electoral_district.html - documentation
* ESPG.postman_collection.json - collection file for Postman used for testing espg.io API queries.

### Project files

* import_geodata.py - reads lfed000a16g_e.gml, calculates central points from boundaries coordinates, writes lfed000a16g_e.csv
* lfed000a16g_e.csv - contains information abount FEDs (id, name, province, central coordinate in NAD83)
* convert_coordinates.py - reads lfed000a16g_e.csv, converts central coordinates from NAD83 to GPS coordinates, writes geodata.csv
* geodata.csv - data set with information abous FEDs (id, name, province, central coordinates) suitable for use with Google Maps API
