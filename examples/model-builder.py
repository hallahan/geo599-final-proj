# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# model.py
# Created on: 2013-03-13 17:53:49.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: model <Output_Cell_Size> <Reclassification__2_> <ls_recls100> <rcls_slo100> <clipped_slido_shp__2_> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

# Script arguments
Output_Cell_Size = arcpy.GetParameterAsText(0)
if Output_Cell_Size == '#' or not Output_Cell_Size:
    # Output_Cell_Size = "8.89237760700743" # provide a default value if unspecified
    Output_Cell_Size = "100" # provide a default value if unspecified

Reclassification__2_ = arcpy.GetParameterAsText(1)
if Reclassification__2_ == '#' or not Reclassification__2_:
    Reclassification__2_ = "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12" # provide a default value if unspecified

ls_recls100 = arcpy.GetParameterAsText(2)
if ls_recls100 == '#' or not ls_recls100:
    ls_recls100 = "C:\\gis-prog-proj\\output\\ls_recls100" # provide a default value if unspecified

rcls_slo100 = arcpy.GetParameterAsText(3)
if rcls_slo100 == '#' or not rcls_slo100:
    rcls_slo100 = "C:\\gis-prog-proj\\output\\rcls_slo100" # provide a default value if unspecified

clipped_slido_shp__2_ = arcpy.GetParameterAsText(4)
if clipped_slido_shp__2_ == '#' or not clipped_slido_shp__2_:
    clipped_slido_shp__2_ = "C:\\gis-prog-proj\\input\\Slido\\clipped_slido.shp" # provide a default value if unspecified

# Local variables:
v10m_slope = "C:\\gis-prog-proj\\input\\10m_slope"
zo_ls100 = clipped_slido_shp__2_
Output_Cell_Size__2_ = "100 100"
Resampling_Technique = "BILINEAR"
Reclassification = "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17"
sl_resamp2 = "C:\\gis-prog-proj\\intermediate\\sl_resamp2"

# Process: Resample
arcpy.Resample_management(v10m_slope, sl_resamp2, Output_Cell_Size__2_, Resampling_Technique)

# Process: Reclassify
arcpy.Reclassify_3d(sl_resamp2, "Value", Reclassification, rcls_slo100, "DATA")

# Process: Zonal Statistics
arcpy.gp.ZonalStatistics_sa(clipped_slido_shp__2_, "FID", sl_resamp2, zo_ls100, "MEAN", "DATA")

# Process: Reclassify (2)
arcpy.Reclassify_3d(zo_ls100, "Value", Reclassification__2_, ls_recls100, "DATA")
