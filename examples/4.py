dir_input           = "C:/gis-prog-proj/input/"
dir_intermediate    = "C:/gis-prog-proj/intermediate/"
dir_output          = "C:/gis-prog-proj/output/"
slope_rcls_mapping  = "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17"
aspect_rcls_mapping = "-1 0 1;0 45 2;45 90 3;90 135 4;135 180 5;180 225 6;225 270 7;270 315 8;315 360 9" 
ndvi_rcls_mapping   = "-100 1;-100 -90 2;-90 -80 3;-80 -70 4;-70 -60 5;-60 -50 6;-50 -40 7;-40 -30 8;-30 -20 9;-20 -10 10;-10 0 11;0 10 12;10 20 13;20 30 14;30 40 15;40 50 16;50 60 17;60 70 18;70 80 19;80 90 20;90 100 21"

import arcpy
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

# note: reclassifying takes a very long time
print("Processing the original original rasters before resampling...")
arcpy.Reclassify_3d(dir_input+"10m_slope",  "Value", slope_rcls_mapping,  dir_output+"rclsSl10" , "DATA")
arcpy.Reclassify_3d(dir_input+"10m_aspect", "Value", aspect_rcls_mapping, dir_output+"rclsAsp10", "DATA")
arcpy.Reclassify_3d(dir_input+"ndvi_int",   "Value", ndvi_rcls_mapping,   dir_output+"rclsNdvi30","DATA")
print("Reclassifying original Slope, Aspect, and NDVI complete.")

zonal_stats_slope_raster  = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_input+"10m_slope",  "MEAN", "DATA")
zonal_stats_aspect_raster = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_input+"10m_aspect", "MEAN", "DATA")
zonal_stats_ndvi_raster   = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_input+"ndvi_int",   "MEAN", "DATA")
print("Generating Zonal Statistics of original Slope, Aspect, NDVI complete.")

arcpy.Reclassify_3d(zonal_stats_slope_raster,  "Value", slope_rcls_mapping,  dir_output+"zsRclsSl10" ,  "DATA")
arcpy.Reclassify_3d(zonal_stats_aspect_raster, "Value", aspect_rcls_mapping, dir_output+"zsRclsAsp10",  "DATA")
arcpy.Reclassify_3d(zonal_stats_ndvi_raster,   "Value", ndvi_rcls_mapping,   dir_output+"zsRclsNdvi30", "DATA")
print("Reclassifying of Zonal Statistics raster of original Slope, Aspect, NDVI complete.")

# 10m rasters resampled into the following resolutions and then processed
for res in ['5', '30', '100', '200']:
    arcpy.Resample_management(dir_input+"10m_slope",  dir_intermediate+"rsmpSl"+res,   res, "BILINEAR")
    arcpy.Resample_management(dir_input+"10m_aspect", dir_intermediate+"rsmpAsp"+res,  res, "BILINEAR")
    print("Resampled Slope and Aspect from 10m to " + res + "m.")

    arcpy.Reclassify_3d(dir_intermediate+"rsmpSl" +res,"Value", slope_rcls_mapping, dir_output+"rclsSl" +res, "DATA")
    arcpy.Reclassify_3d(dir_intermediate+"rsmpAsp"+res,"Value", aspect_rcls_mapping,dir_output+"rclsAsp"+res, "DATA")
    print("Reclassifying Slope and Aspect complete. ("+res+"m)")

    zonal_stats_slope_raster  = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_intermediate+"rsmpSl"+res, "MEAN", "DATA")
    zonal_stats_aspect_raster = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_intermediate+"rsmpSl"+res, "MEAN", "DATA")
    print("Generating Zonal Statistics of Slope and Aspect complete. ("+res+"m)")

    arcpy.Reclassify_3d(zonal_stats_slope_raster, "Value", slope_rcls_mapping, dir_output+"zsRclsSl" +res, "DATA")
    arcpy.Reclassify_3d(zonal_stats_aspect_raster,"Value", aspect_rcls_mapping,dir_output+"zsRclsAsp"+res, "DATA")
    print("Reclassifying of Zonal Statistics raster of Slope and Aspect complete. ("+res+")")


# NDVI raster is in 30m resolution, so it gets resampled to the following resolutions and processed
for res in ['5', '10', '100', '200']:
    arcpy.Resample_management(dir_input+"ndvi_int", dir_intermediate+"rsmpNdvi"+res, res, "BILINEAR")
    print("Resampled NDVI from 30m to " + res + "m.")

    arcpy.Reclassify_3d("ndvi_int","Value", ndvi_rcls_mapping, dir_output+"rclsNdvi","DATA")
    print("Reclassifying NDVI complete. (" + res + "m)")

    zonal_stats_ndvi_raster = arcpy.sa.ZonalStatistics(dir_input+"Slido/clipped_slido.shp", "FID", dir_intermediate+"rsmpNdvi"+res, "MEAN", "DATA")
    print("Generating Zonal Statistics of NDVI complete. (" + res + ")")

    arcpy.Reclassify_3d(zonal_stats_ndvi_raster, "Value", ndvi_rcls_mapping, dir_output+"zsRclsAsp"+res, "DATA")
    print("Reclassifying of Zonal Statistics raster of NDVI complete. (" + res + ")")
