# Nicholas Hallahan
# Rubini Mahalingnam
# GEO599 Final Project
# Wed Mar 20 2013
# GNU GPLv3 License
# http://en.wikipedia.org/wiki/GNU_General_Public_License

# This is the arcpy interface class. This class does
# all of the direct work of using the arcpy module.

# It provides printing to stdout of the status of tasks
# so the user can see what the tool is working on. 

# It also provides exception handling if an arcpy
# processing task fails.

import sys
import traceback

try:
    # Import arcpy module
    print('Importing arcpy...')
    import arcpy
    print('Done importing arcpy!')
except Exception, err: 
    raise Exception("UNABLE TO LOAD ARCPY! Check to see that ArcGIS is installed and has a valid license.")

class ArcpyInterface: 

    def __init__(self, dir_input, dir_intermediate, dir_output):
        """
        Given the input, intermediate, and output directory paths, all of the
        paths to the files used by this tool are set up. Also, 3D Analyst and
        the Spatial extensions are checked out and loaded.
        """

        # setting directory paths
        self.dir_input = dir_input
        self.dir_intermediate = dir_intermediate
        self.dir_output = dir_output

        ################# INPUT PATHS ########################
        # shapefile containing the location of all landslides in oregon
        self.landslide_shp = dir_input + "Slido/clipped_slido.shp"

        # Slope LIDAR Raster with 10x10m resolution
        self.input_slope = dir_input + "10m_slope"

        # Aspect LIDAR Raster with 10x10m resolution
        self.input_aspect = dir_input+"10m_aspect"

        # NDVI Landsat Raster with 30x30m resolution
        self.input_ndvi = dir_input+"ndvi_int"
        ######################################################

        try:
            arcpy.CheckOutExtension("3D") # make sure that 3D analyst is checked out
            arcpy.CheckOutExtension("Spatial") # make sure the spatial analyst is checked out
        except Exception, err:
            raise Exception("3D/SPATIAL ANALYST ERROR: You either dont have Spatial Analyst or you need to pay for a license...")
    

    def set_reclassification_mapping(self, slope_mapping, aspect_mapping, ndvi_mapping):
        """
        This sets the mapping to separate groups for the
        reclassification processing.
        """
        self.slope_mapping = slope_mapping
        self.aspect_mapping = aspect_mapping
        self.ndvi_mapping = ndvi_mapping


    def process_slope(self, resolutions):
        """
        All of the processing steps for the slope
        raster are performed. It is designed to be 
        run in parallel with the other processing 
        functions via multiprocessing.

        Resolutions is an array of strings that specify
        the resolutions the rasters will be resampled to.
        """
        print("Beginning to process SLOPE...")

        print("Slope: Reclassifying raster... (original raster)")
        arcpy.Reclassify_3d(self.input_slope,  "Value", self.slope_mapping,  self.dir_output+"rclsSl10" , "DATA")
        print("Slope: Processing Zonal Stats... (original raster)")
        zonal_stats_slope_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.input_slope, "MEAN", "DATA")
        print("Slope: Reclassifying Zonal Stats... (original raster)")
        arcpy.Reclassify_3d(zonal_stats_slope_raster, "Value", self.slope_mapping, self.dir_output+"zsRclsSl10",  "DATA")

        for res in resolutions:
            print("Slope: Resampling to " + res + "m raster...")
            arcpy.Resample_management(self.input_slope, self.dir_intermediate+"rsmpSl"+res,  res, "BILINEAR")
            print("Slope: Reclassifying to " + res + "m raster...")
            arcpy.Reclassify_3d(self.dir_intermediate+"rsmpSl"+res,"Value", self.slope_mapping, self.dir_output+"rclsSl"+res, "DATA")
            print("Slope: Processing Zonal Stats... (" + res + "m)")
            zonal_stats_slope_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.dir_intermediate+"rsmpSl"+res, "MEAN", "DATA")
            print("Slope: Reclassifying Zonal Stats... (" + res + "m)")
            arcpy.Reclassify_3d(zonal_stats_slope_raster,"Value", self.slope_mapping, self.dir_output+"zsRclsSl"+res, "DATA")

        print("Finished processing SLOPE.")


    def process_aspect(self, resolutions):
        """
        All of the processing steps for the aspect
        raster are performed. It is designed to be 
        run in parallel with the other processing 
        functions via multiprocessing.

        Resolutions is an array of strings that specify
        the resolutions the rasters will be resampled to.
        """
        print("Beginning to process ASPECT...")

        print("Aspect: Reclassifying aspect raster... (original raster)")
        arcpy.Reclassify_3d(self.input_aspect, "Value", self.aspect_mapping, self.dir_output+"rclsAsp10", "DATA")
        print("Aspect: Processing Zonal Stats... (original raster)")
        zonal_stats_aspect_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.input_aspect, "MEAN", "DATA")
        print("Aspect: Reclassifying Zonal Stats... (original raster)")
        arcpy.Reclassify_3d(zonal_stats_aspect_raster, "Value", self.aspect_mapping, self.dir_output+"zsRclsAsp10",  "DATA")

        for res in resolutions:
            print("Aspect: Resampling to " + res + "m raster...")
            arcpy.Resample_management(self.input_aspect, self.dir_intermediate+"rsmpAsp"+res,  res, "BILINEAR")
            print("Aspect: Reclassifying to " + res + "m raster...")
            arcpy.Reclassify_3d(self.dir_intermediate+"rsmpAsp"+res,"Value", self.aspect_mapping, self.dir_output+"rclsAsp"+res, "DATA")
            print("Aspect: Processing Zonal Stats... (" + res + "m)")
            zonal_stats_aspect_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.dir_intermediate+"rsmpAsp"+res, "MEAN", "DATA")
            print("Aspect: Reclassifying Zonal Stats... (" + res + "m)")
            arcpy.Reclassify_3d(zonal_stats_aspect_raster,"Value", self.aspect_mapping, self.dir_output+"zsRclsAsp"+res, "DATA")

        print("Finished processing ASPECT.")


    def process_ndvi(self, resolutions):
        """
        All of the processing steps for the NDVI
        raster are performed. It is designed to be 
        run in parallel with the other processing 
        functions via multiprocessing.

        Resolutions is an array of strings that specify
        the resolutions the rasters will be resampled to.
        """
        # print("Beginning to process NDVI...")

        # print("NDVI: Reclassifying raster... (original raster)")
        # arcpy.Reclassify_3d(self.input_ndvi, "Value", self.ndvi_mapping, self.dir_output+"rclsNdvi30", "DATA")
        # print("NDVI: Processing Zonal Stats... (original raster)")
        # zonal_stats_ndvi_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.input_ndvi, "MEAN", "DATA")
        # print("NDVI: Reclassifying Zonal Stats... (original raster)")
        # arcpy.Reclassify_3d(zonal_stats_ndvi_raster, "Value", self.ndvi_mapping, self.dir_output+"zsRclsNdvi30",  "DATA")

        for res in resolutions:
            print("NDVI: Resampling to " + res + "m raster...")
            arcpy.Resample_management(self.input_ndvi, self.dir_intermediate+"rsmpNdvi"+res,  res, "BILINEAR")
            print("NDVI: Reclassifying to " + res + "m raster...")
            arcpy.Reclassify_3d(self.dir_intermediate+"rsmpNdvi"+res,"Value", self.ndvi_mapping, self.dir_output+"rclsNdvi"+res, "DATA")
            print("NDVI: Processing Zonal Stats... (" + res + "m)")
            zonal_stats_ndvi_raster = arcpy.sa.ZonalStatistics(self.landslide_shp, "FID", self.dir_intermediate+"rsmpNdvi"+res, "MEAN", "DATA")
            print("NDVI: Reclassifying Zonal Stats... (" + res + "m)")
            arcpy.Reclassify_3d(zonal_stats_ndvi_raster,"Value", self.ndvi_mapping, self.dir_output+"zsRclsNdvi"+res, "DATA")

        print("Finished processing NDVI.")

