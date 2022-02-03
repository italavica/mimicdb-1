import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb

useful_records=[]

with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/RECORDS') as f:
    records_list = f.readlines()


for e in range(10): #add a function that verifies the file format .hea
    e=e+1
    print(e)
    path = "/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/" + records_list[e]
    print(path)
    path= str.rstrip(path)
    signal, fields = wfdb.rdsamp(path)                                   
    sig_name= fields["sig_name"]

    if ('ABPmean'in sig_name) and ('ABPsys' in sig_name) and ('ABPdias' in sig_name) and ('PLETH' in sig_name):
        print("exists")
        useful_records.append(path)

    else:
        print("does not exist")

print(useful_records)



# for e in sig_name:
#     if( e == 'ABPmean') and (e== "Pleth"):
#         print("ABP mean exists")
#     else: 
#         print("don't exist")






