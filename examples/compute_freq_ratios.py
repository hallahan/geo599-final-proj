# Nicholas Hallahan
# Rubini Mahalingnam
# GEO599 Final Project
# Wed Mar 20 2013
# GNU GPLv3 License
# http://en.wikipedia.org/wiki/GNU_General_Public_License

# Rather than concatenating numbers to the strings to compute
# the paths of all of the rasters we will be looking at, it
# is more clear to just see the complete paths. This was easily
# done using the multi-cursor editing functionality of Sublime
# Text 2.

# reclassified slope raster paths
rcls_sl_5    = r"D:\gis-prog-proj\output\rclssl5"
rcls_sl_10   = r"D:\gis-prog-proj\output\rclssl10" 
rcls_sl_30   = r"D:\gis-prog-proj\output\rclssl30"
rcls_sl_100  = r"D:\gis-prog-proj\output\rclssl100"
rcls_sl_200  = r"D:\gis-prog-proj\output\rclssl200"

# reclassified aspect raster paths
rcls_asp_5   = r"D:\gis-prog-proj\output\rclsasp5"
rcls_asp_10  = r"D:\gis-prog-proj\output\rclsasp10" 
rcls_asp_30  = r"D:\gis-prog-proj\output\rclsasp30"
rcls_asp_100 = r"D:\gis-prog-proj\output\rclsasp100"
rcls_asp_200 = r"D:\gis-prog-proj\output\rclsasp200"

# reclassified NDVI raster paths
rcls_ndvi_5   = r"D:\gis-prog-proj\output\rclsndvi5"
rcls_ndvi_10  = r"D:\gis-prog-proj\output\rclsndvi10" 
rcls_ndvi_30  = r"D:\gis-prog-proj\output\rclsndvi30"
rcls_ndvi_100 = r"D:\gis-prog-proj\output\rclsndvi100"
rcls_ndvi_200 = r"D:\gis-prog-proj\output\rclsndvi200"

# reclassified Zonal Statistics slope raster paths
rcls_zs_sl_5    = r"D:\gis-prog-proj\output\zsrclssl5"
rcls_zs_sl_10   = r"D:\gis-prog-proj\output\zsrclssl10" 
rcls_zs_sl_30   = r"D:\gis-prog-proj\output\zsrclssl30"
rcls_zs_sl_100  = r"D:\gis-prog-proj\output\zsrclssl100"
rcls_zs_sl_200  = r"D:\gis-prog-proj\output\zsrclssl200"

# reclassified Zonal Statistics aspect raster paths
rcls_zs_asp_5   = r"D:\gis-prog-proj\output\zsrclsasp5"
rcls_zs_asp_10  = r"D:\gis-prog-proj\output\zsrclsasp10" 
rcls_zs_asp_30  = r"D:\gis-prog-proj\output\zsrclsasp30"
rcls_zs_asp_100 = r"D:\gis-prog-proj\output\zsrclsasp100"
rcls_zs_asp_200 = r"D:\gis-prog-proj\output\zsrclsasp200"

# reclassified Zonal Statistics NDVI raster paths
rcls_zs_ndvi_5   = r"D:\gis-prog-proj\output\zsrclsndvi5"
rcls_zs_ndvi_10  = r"D:\gis-prog-proj\output\zsrclsndvi10" 
rcls_zs_ndvi_30  = r"D:\gis-prog-proj\output\zsrclsndvi30"
rcls_zs_ndvi_100 = r"D:\gis-prog-proj\output\zsrclsndvi100"
rcls_zs_ndvi_200 = r"D:\gis-prog-proj\output\zsrclsndvi200"

import arcpy
arcpy.CheckOutExtension("Spatial")


for rows in arcpy.SearchCursor(rcls_sl_5       ):

for rows in arcpy.SearchCursor(rcls_sl_10      ):

for rows in arcpy.SearchCursor(rcls_sl_30      ):

for rows in arcpy.SearchCursor(rcls_sl_100     ):

for rows in arcpy.SearchCursor(rcls_sl_200     ):

for rows in arcpy.SearchCursor(rcls_asp_5      ):

for rows in arcpy.SearchCursor(rcls_asp_10     ):

for rows in arcpy.SearchCursor(rcls_asp_30     ):

for rows in arcpy.SearchCursor(rcls_asp_100    ):

for rows in arcpy.SearchCursor(rcls_asp_200    ):

for rows in arcpy.SearchCursor(rcls_ndvi_5     ):

for rows in arcpy.SearchCursor(rcls_ndvi_10    ):

for rows in arcpy.SearchCursor(rcls_ndvi_30    ):

for rows in arcpy.SearchCursor(rcls_ndvi_100   ):

for rows in arcpy.SearchCursor(rcls_ndvi_200   ):

for rows in arcpy.SearchCursor(rcls_zs_sl_5    ):

for rows in arcpy.SearchCursor(rcls_zs_sl_10   ):

for rows in arcpy.SearchCursor(rcls_zs_sl_30   ):

for rows in arcpy.SearchCursor(rcls_zs_sl_100  ):

for rows in arcpy.SearchCursor(rcls_zs_sl_200  ):

for rows in arcpy.SearchCursor(rcls_zs_asp_5   ):

for rows in arcpy.SearchCursor(rcls_zs_asp_10  ):

for rows in arcpy.SearchCursor(rcls_zs_asp_30  ):

for rows in arcpy.SearchCursor(rcls_zs_asp_100 ):

for rows in arcpy.SearchCursor(rcls_zs_asp_200 ):

for rows in arcpy.SearchCursor(rcls_zs_ndvi_5  ):

for rows in arcpy.SearchCursor(rcls_zs_ndvi_10 ):

for rows in arcpy.SearchCursor(rcls_zs_ndvi_30 ):

for rows in arcpy.SearchCursor(rcls_zs_ndvi_100):

for rows in arcpy.SearchCursor(rcls_zs_ndvi_200):


# bins_rcls_sl_5       
# bins_rcls_sl_10      
# bins_rcls_sl_30      
# bins_rcls_sl_100     
# bins_rcls_sl_200     
# bins_rcls_asp_5      
# bins_rcls_asp_10     
# bins_rcls_asp_30     
# bins_rcls_asp_100    
# bins_rcls_asp_200    
# bins_rcls_ndvi_5     
# bins_rcls_ndvi_10    
# bins_rcls_ndvi_30    
# bins_rcls_ndvi_100   
# bins_rcls_ndvi_200   
# bins_rcls_zs_sl_5    
# bins_rcls_zs_sl_10   
# bins_rcls_zs_sl_30   
# bins_rcls_zs_sl_100  
# bins_rcls_zs_sl_200  
# bins_rcls_zs_asp_5   
# bins_rcls_zs_asp_10  
# bins_rcls_zs_asp_30  
# bins_rcls_zs_asp_100 
# bins_rcls_zs_asp_200 
# bins_rcls_zs_ndvi_5  
# bins_rcls_zs_ndvi_10 
# bins_rcls_zs_ndvi_30 
# bins_rcls_zs_ndvi_100
# bins_rcls_zs_ndvi_200