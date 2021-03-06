import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb
from time import sleep
from tqdm import tqdm

useful_records=[]



with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/RECORDS') as f:
    folder_list = f.readlines()

for folder in tqdm(folder_list):
    path_folder = '/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/' + folder
    path_folder= str.rstrip(path_folder)
    path_folder_records= path_folder + "RECORDS"

    with open(path_folder_records) as f:
        records_list = f.readlines()


    for file in records_list: 
        path = path_folder + file
        path= str.rstrip(path)
        path_dat= path + ".dat"

        if os.path.exists(path_dat):
 
            signal, fields = wfdb.rdsamp(path)                                   
            sig_name= fields["sig_name"]

            if ('ABPmean'in sig_name) and ('ABPsys' in sig_name) and ('ABPdias' in sig_name) and ('PLETH' in sig_name):
                useful_records.append(path) 


print(useful_records)

with open('useful_records.txt', 'w') as f:

    for record in useful_records:
        f.write(record)
        f.write('\n')










