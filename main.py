# Nicholas Hallahan
# Rubini Mahalingnam
# GEO599 Final Project
# Wed Mar 20 2013
# GNU GPLv3 License
# http://en.wikipedia.org/wiki/GNU_General_Public_License

# This is the main script that is to be executed by the user.
# This uses ArcpyInterface to do the processing. Here we handle
# all of the input strings and parameters and also handle
# multiprocessing.

import sys
import traceback
import os
import shutil
import multiprocessing
from datetime import datetime


############ DEFAULT DIRECTORY PATHS #########################
# If no folder paths are specified as arguments to the script,
# then these paths will be used by default.
dir_input           = "D:/gis-prog-proj/input/"
dir_intermediate    = "D:/gis-prog-proj/intermediate/"
dir_output          = "D:/gis-prog-proj/output/"
##############################################################

############ DEFAULT INTERVALS FOR RECLASSIFICATION ##########
# These strings specify the intervals in which we reclassify
# rasters for slope, aspect, and NDVI. If you wish to have a
# different classification scale, the new parameters should be
# specified here.
slope_mapping  = "0 5 1;5 10 2;10 15 3;15 20 4;20 25 5;25 30 6;30 35 7;35 40 8;40 45 9;45 50 10;50 55 11;55 60 12;60 65 13;65 70 14;70 75 15;75 80 16;80 85 17"
aspect_mapping = "-1 0 1;0 45 2;45 90 3;90 135 4;135 180 5;180 225 6;225 270 7;270 315 8;315 360 9" 
ndvi_mapping   = "-100 1;-100 -90 2;-90 -80 3;-80 -70 4;-70 -60 5;-60 -50 6;-50 -40 7;-40 -30 8;-30 -20 9;-20 -10 10;-10 0 11;0 10 12;10 20 13;20 30 14;30 40 15;40 50 16;50 60 17;60 70 18;70 80 19;80 90 20;90 100 21"
##############################################################

############ DEFAULT RESAMPLING RESOLUTIONS###################
# These are the resolutions that each raster is resampled to
slope_resolutions  = ['5', '30', '100', '200'] # orig slope is 10m
aspect_resolutions = ['5', '30', '100', '200'] # orig aspect is 10m
ndvi_resolutions   = ['5', '10', '100', '200'] # orig ndvi is 30m
##############################################################


if __name__ == '__main__':
    try:
        # If we have specified the paths for the input, intermediate,
        # and output directories in the command line, we set the paths
        # accordingly.
        if len(sys.argv) is 4:
            if dir_input[-1] != '/' or dir_input[-1] != '\\':
                dir_input = dir_input + '\\'
            if dir_intermediate[-1] != '/' or dir_intermediate[-1] != '\\':
                dir_intermediate = dir_intermediate + '\\'
            if dir_output[-1] != '/' or dir_output[-1] != '\\':
                dir_output = dir_output + '\\'

        # Checking to see if the directory paths are valid
        if os.path.isdir(dir_input) is False:
            print("Invalid input directory.")
            print("Please specify a directory with your input files that exists.")
            print("EXITING...")
            sys.exit()

        if os.path.isdir(dir_intermediate) is False:
            print("Invalid intermediate directory.")
            print("Please specify an empty directory for your intermediate files that exists.")
            print("EXITING...")
            sys.exit()

        if os.path.isdir(dir_output) is False:
            print("Invalid output directory.")
            print("Please specify an empty directory for your output files that exists.")
            print("EXITING...")
            sys.exit()

        # Uncomment this if you want to have the script be able to delete the intermediate
        # and output directories. I removed this by request of Charles.

        # if len(os.listdir(dir_intermediate)) > 0:
        #     print("The intermediate directory is not empty.")
        #     resp = raw_input("Would you like to delete the contents of: " + dir_intermediate + " (y/n)?")
        #     if resp is 'y' or resp is 'yes':
        #         shutil.rmtree(dir_intermediate)
        #         os.mkdir(dir_intermediate)
        #     else:
        #         print("EXITING!")
        #         sys.exit()

        # if len(os.listdir(dir_output)) > 0:
        #     print("The output directory is not empty.")
        #     resp = raw_input("Would you like to delete the contents of: " + dir_output + " (y/n)?")
        #     if resp is 'y' or resp is 'yes':
        #         shutil.rmtree(dir_output)
        #         os.mkdir(dir_output)
        #     else:
        #         print("EXITING!")
        #         sys.exit()

        # importing the ArcpyInterface that interfaces with arcpy
        from ArcpyInterface import ArcpyInterface

        # setting up object
        arcObj = ArcpyInterface(dir_input, dir_intermediate, dir_output)
        arcObj.set_reclassification_mapping(slope_mapping, aspect_mapping, ndvi_mapping)

        # single proccess mode of execution
        print("Starting batch processing...")
        print(str(datetime.now()))
        # arcObj.process_slope(slope_resolutions)
        # arcObj.process_aspect(aspect_resolutions)
        arcObj.process_ndvi(ndvi_resolutions)

        # multiprocessing mode of execution

        # This way of executing 3 functions in parallel as child processes works, but
        # there is a bug with ArcGIS licensing. arcpy exits when it detects that multiple
        # processes are utilizing the library.

        # specifying separate processes to do the work in parallel
        # slope_proc  = multiprocessing.Process(target=arcObj.process_slope, args=(slope_resolutions,))
        # aspect_proc = multiprocessing.Process(target=arcObj.process_aspect, args=(aspect_resolutions,))
        # ndvi_proc   = multiprocessing.Process(target=arcObj.process_ndvi, args=(ndvi_resolutions,))

        # # 3 child proc are now executing
        # slope_proc.start()
        # aspect_proc.start()
        # ndvi_proc.start()

        # slope_proc.join() # waiting for slope proc to finish
        # print("SLOPE Processing Complete!")
        # aspect_proc.join() # waiting for aspect proc to finish
        # print("ASPECT Processing Complete!")
        # ndvi_proc.join()
        # print("NDVI Processing Complete!")

        print("ALL PROCESSING FINISHED. EXITING...")
        print(str(datetime.now()))
        
    except Exception as e:
        print("Sorry, an error has occurred:"+format(e))
        exc_type, exc_value, exc_traceback =sys.exc_info()
        print(exc_type)
        print(exc_value)
        traceback.print_tb(exc_traceback, limit=10)