import pandas as ps
import os

"""
Python program to merge CSV files which total row count is greater than 1 million

Required structure for this to work:

    root
    ->  subfolder_1
    -   ->  fileA.csv
    -   ->  fileB.csv
    ->  subfolder_2
    -   ->  fileA.csv
    -   ->  fileB.csv
    ...and so on.

    This code merges File A with File B for each subdirectory
    Merged files are saved in root folder:
        root
        ->subfolder_X_merged.csv.

"""


root ='main_folder/src'         #change this depending on where your current working directory
folders = os.listdir(root)      #get a list of all the subdirectories
files = {}                      #save all the files


for folder in folders:
   files[folder] = os.listdir(root+folder)


for key in files:
    print("Working on " + key)
    file_a = files[key][0]
    file_b = files[key][1]
    print("Merging:\n"+file_a+ " + "+file_b)
    full_path_a = root+key+'/'+file_a
    full_path_b = root+key+'/'+file_b
    a_csv = ps.read_csv(full_path_a,low_memory = False,keep_default_na=False)
    b_csv = ps.read_csv(full_path_b,low_memory = False,keep_default_na=False)
    to_merge = {0:a_csv,1:b_csv}
    result =  ps.concat(to_merge, ignore_index =True)
    merged_name = key+'_merged.csv'
    result.to_csv(root+'/'+merged_name)
