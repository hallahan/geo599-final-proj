resampling_resolutions = ['5', '10', '30', '100', '200']


import arcpy
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

for res in resampling_resolutions:
    arcpy.Resample_management("C:/gis-prog-proj/input/10m_slope",  "C:/gis-prog-proj/intermediate/rsmpSl"+res,   res, "BILINEAR")
    arcpy.Resample_management("C:/gis-prog-proj/input/10m_aspect", "C:/gis-prog-proj/intermediate/rsmpAsp"+res,  res, "BILINEAR")
    arcpy.Resample_management("C:/gis-prog-proj/input/ndvi_int",   "C:/gis-prog-proj/intermediate/rsmpNdvi"+res, res, "BILINEAR")

    arcpy.Reclassify_3d("C:/gis-prog-proj/intermediate/rsmpSl"+res, "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "C:/gis-prog-proj/output/rclsSl"+res, "DATA")
    zonal_stats_raster = arcpy.sa.ZonalStatistics("C:/gis-prog-proj/input/Slido/clipped_slido.shp", "FID", "C:/gis-prog-proj/intermediate/rsmpSl"+res, "MEAN", "DATA")
    arcpy.Reclassify_3d(zonal_stats_raster, "Value", "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17", "C:/gis-prog-proj/output/rclsSlZs"+res, "DATA")
