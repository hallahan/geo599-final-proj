import arcpy
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

arcpy.Resample_management("C:/gis-prog-proj/input/10m_aspect", "C:/gis-prog-proj/intermediate/rsmpAsp",  '100', "BILINEAR")
arcpy.Resample_management("C:/gis-prog-proj/input/ndvi_int",   "C:/gis-prog-proj/intermediate/rsmpNdvi", '100', "BILINEAR")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "rsmpasp"
# reclassify for aspect, includes needed intervals
arcpy.gp.Reclassify_sa("rsmpasp","Value","-1 0 1;0 45 2;45 90 3;90 135 4;135 180 5;180 225 6;225 270 7;270 315 8;315 360 9","C:/gis-prog-proj/output/rcls","DATA")

# on ruby's machine
# reclassify for ndvi
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "ndvi_int"
arcpy.Reclassify_3d("ndvi_int","VALUE","-100 1;-100 -90 2;-90 -80 3;-80 -70 4;-70 -60 5;-60 -50 6;-50 -40 7;-40 -30 8;-30 -20 9;-20 -10 10;-10 0 11;0 10 12;10 20 13;20 30 14;30 40 15;40 50 16;50 60 17;60 70 18;70 80 19;80 90 20;90 100 21","J:/frequency_ratio/NEW_start/delme/rcls_ndvi","DATA")


# arcpy.Reclassify_3d("C:/gis-prog-proj/intermediate/resample", "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "C:/gis-prog-proj/output/slope-reclass", "DATA")
# zonal_stats_raster = arcpy.sa.ZonalStatistics("C:/gis-prog-proj/input/Slido/clipped_slido.shp", "FID", "C:/gis-prog-proj/intermediate/resample", "MEAN", "DATA")
# arcpy.Reclassify_3d(zonal_stats_raster, "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "C:/gis-prog-proj/output/ls-reclass", "DATA")
