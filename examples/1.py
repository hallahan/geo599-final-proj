import arcpy
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")
print "resampling"
arcpy.Resample_management("D:/gis-prog-proj/input/10m_slope", "D:/gis-prog-proj/intermediate/resample", "100 100", "BILINEAR")
print "reclassify"
arcpy.Reclassify_3d("D:/gis-prog-proj/intermediate/resample", "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "D:/gis-prog-proj/output/slope-reclass", "DATA")
print "zs"
zonal_stats_raster = arcpy.sa.ZonalStatistics("D:/gis-prog-proj/input/Slido/clipped_slido.shp", "FID", "D:/gis-prog-proj/intermediate/resample", "MEAN", "DATA")
print "reclass again"
arcpy.Reclassify_3d(zonal_stats_raster, "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "D:/gis-prog-proj/output/ls-reclass", "DATA")
