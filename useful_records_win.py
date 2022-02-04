import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb

useful_records=[]

with open('C:/Users/ezxiaav/Documents/Databases/mimic-database-1.0.0/037\RECORDS') as f:
    records_list = f.readlines()


for file in records_list: #add a function that verifies the file format .hea
    path = "C:/Users/ezxiaav/Documents/Databases/mimic-database-1.0.0/037/" + file
    path= str.rstrip(path)
    print(path)
    path_dat= path + ".dat"
    if os.path.exists(path_dat):

        signal, fields = wfdb.rdsamp(path)                                   
        sig_name= fields["sig_name"]

        if ('ABPmean'in sig_name) and ('ABPsys' in sig_name) and ('ABPdias' in sig_name) and ('PLETH' in sig_name):
            useful_records.append(path)


print(useful_records)
 


# for e in sig_name:
#     if( e == 'ABPmean') and (e== "Pleth"):
#         print("ABP mean exists")
#     else: 
#         print("don't exist")






