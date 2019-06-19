# Merge_Million_CSV
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
