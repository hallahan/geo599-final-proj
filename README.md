#Overview

This python script automates the processing of several large
LIDAR and Landsat datasets. A batch script is required, as opposed
to an ArcGIS tool, because the rasters take a very long time to
display in Arc, and the processing takes several hours. This is not
a reasonable amount of time to wait for a tool, so a batch script
is used instead.

#Usage

Make sure you have set your python path to be the python executable that ArcGIS uses. The only python library you need to have installed
is arcpy.

NOTE: This script processes 65GB of data. Make sure you have this much
hard drive space availible. Also, this tool will require about 5 hours
of run time.

You may just run the tool with no args if you have the following paths for your input, intermediate, and output directories:

INPUT:
```
D:/gis-prog-proj/input/
```

INTERMEDIATE:
```
D:/gis-prog-proj/intermediate/
```

OUTPUT:
```
D:/gis-prog-proj/output/
```

All input rasters that will be processed should be in the input
directory. The intermediate and output directories need to be empty.

To run the script, you execute main.py:
```
python main.py
```

You may pipe the output of the tool to a log file as follows:
python main.py > log.txt

Alternatively, you can specify the input, intermediate, and output
directories. This is useful if you are low on hard drive space. All
three folder paths must be specified.

```
python main.py <input-dir> <intermediate-dir> <output-dir>
```

NOTE: The intermediate directory requires the most space (42GB).


#Outputs

The output rasters are in the `output` directory. The naming convention
is somewhat cryptic, because the arcpy tool only allows a maximum of
13 characters for file names.

All directories that begin with `rcls` are the reclassified rasters
that did not run through Zonal Statistiscs.

All directories that begin with `zsrcls` are reclassified rasters
that DID run through Zonal Statistics.

The after rcls is `asp`, `sl`, or `ndvi`. These are the types of
rasters -- Aspect, Slope, and NDVI, respectively.

The final number defines the resolution of raster. `200` means
"200m x 200m".


#Contributors

Nicholas Hallahan - nick@theoutpost.io

Rubini Mahalingnam - santhans@onid.orst.edu

#License

GNU GPLv3 License http://en.wikipedia.org/wiki/GNU_General_Public_License