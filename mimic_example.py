import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb
from tqdm import tqdm
from read_records import read_records
from check_signal import check_signal

with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/RECORDS') as f:
    lines = f.readlines()
f.close()
f_yes = open('ABP_PLETH.txt', 'w')
f_no = open('NO_ABP_PLETH.txt', 'w')

# path = "/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/" + lines[1]
# path= str.rstrip(path)

#record= wfdb.rdrecord('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/47400002')

# sig_name= fields["sig_name"]

# print(type(sig_name))
# wfdb.plot_wfdb(record=record, title='Example signals')
useful=[]
no_useful=[]
for file in tqdm(lines):
    """path = "/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/" + file
    path= str.rstrip(path) """

    path = read_records(file)
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




# # for e in sig_name:
# #     if( e == 'ABPmean') and (e== "Pleth"):
# #         print("ABP mean exists")
# #     else: 
# #         print("don't exist")

# if ('ABPmean'in sig_name) and ('RESP' in sig_name):
#     print("exists")
# else:
#     print("does not")




