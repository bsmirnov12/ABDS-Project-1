# Geodata subproject

## The goal

* Create visual representation of 2015 House of Commons Elections analysis using Google Maps

* Visually find unobvious regularities in data using the map

## Files

* Subproject documentation:

  * **Readme.md** - this file

  * **Geodata.md** - technical intricacies when processing coordinates data

* Main result

  * **PerCapitaIncome.ipynb** - Jupyter notebook with observations and resulting Google Map for the presentation

  * **Geodata Slides.pptx** - presentation slides for geodata part

* Source data files:

  * Federal Electoral District Boundary Files (contents of lfed000a16g_e.zip)

    * 92-160-g2016002-eng.pdf - format description

    * federal_electoral_district.html - metadata (rather useless)

    * **lfed000a16g_e.gml** - FED boundaries in GML

    * lfed000a16g_e.xsd - XML Schema of lfed000a16g_e.gml

  * Other CSV files from ../data used by PerCapitaIncome.ipynb

* Output data files:

  * **geodata.csv** - GPS coordinates of FEDs central points (for symbol layer on Google Maps)

  * **provinces.csv** - GPS coordinates of Provinces/Territories central points (for marker layer on Google Maps)

* Scripts and intermediate data files

  * import_geodata.py, import_geodata.ipynb - original script and its Jupyter notebook version (as project requirements mandate). Imports **lfed000a16g_e.gml**,
calculates FEDs' central points in the source coordinate system (NAD83), creates **lfed000a16g_e.csv**.

  * lfed000a16g_e.csv - output of the above script, intermediate data with FEDs central point coordinates in NAD83 format (not suitable for Google Maps)

  * convert_coordinates.py, convert_coordinates.ipynb - original script and its Jupyter notebook version (as project requirements mandate).
Reads **lfed000a16g_e.csv**, converts NAD83 coordinates into GPS coordinates using Web API [espg.io](https://epsg.io/).
Creates **geodata.csv** which is later used by **PerCapitaIncome.ipynb**

  * ESPG.postman_collection.json - Postman collection for testing coordinate system conversion using [espg.io](https://epsg.io/) Web API.

  * make_provinces.py, make_provinces.ipynb - original script and its Jupyter notebook version (as project requirements mandate).
Reads **geodata.csv** and creates **provinces.csv** that contains provinces' central points. Late used for putting marks with info boxes on Google Maps.

  * geodata.ipynb - intermediate Jupyter notebook used for testing. Should be discarded

  * Income.ipynb - intermediate result. Should be discarded in favour of **PerCapitaIncome.ipynb**, which is more representative.

  * ./Images - folder to keep images used in the presentation slides, as well as some images necessary for correct display of info boxes in **PerCapitaIncome.ipynb**
