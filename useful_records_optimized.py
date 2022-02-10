import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb
from time import sleep
from tqdm import tqdm
from read_records import read_records
from check_signal import check_signal





with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/RECORDS') as f:
    folder_list = f.readlines()
f.close()

f_yes = open('ABP_PLETH.txt', 'w')
f_no = open('NO_ABP_PLETH.txt', 'w')

for folder in tqdm(folder_list):
    path_folder = '/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/' + folder
    path_folder= str.rstrip(path_folder)
    path_folder_records= path_folder + "RECORDS"

    with open(path_folder_records) as f:
        records_list = f.readlines()
    f.close()


    for file in records_list: 
        path = path_folder + file
        path= str.rstrip(path)
        response = check_signal(path)

        if (response == 1):
            with open('ABP_PLETH.txt', 'a') as f_yes:
                f_yes.write(path + "\n")
        else:
            with open('NO_ABP_PLETH.txt', 'a') as f_no:
                f_no.write(path + "\n")    
        path = ""

f_yes.close()
f_no.close()










