# Geodata information

## The goal

To determine central coordinates of Federal Electoral Districts (FED) suitable for quering Google Maps APIs.

## Data Sources

### Statistics Canada

[Federal Electoral District Boundary Files](https://www150.statcan.gc.ca/n1/en/catalogue/92-171-X)

The geographic coordinates data is proveded in GML (a flavour of XML) format.
The coordinates are represented as Lambert conformal conic projection (North American Datum of 1983 (NAD83))

The boundary file contains following information:
* FED id
* FED name in English and French (separately)
* Province id
* Province name in English and French (in one string)
* A list of coordinates that defines a bound around an FED

### EPSG registry

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
