import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb


with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/RECORDS') as f:
    lines = f.readlines()

print(lines)
path = "/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/" + lines[1]
path= str.rstrip(path)
print(path)
record= wfdb.rdrecord(path)



wfdb.plot_wfdb(record=record, title='Example signals')
record_header = wfdb.rdheader('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/037n',
                               rd_segments=True)
signal, fields = wfdb.rdsamp('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/037n')                               

print(fields)
print(type(fields))

sig_name= fields["sig_name"]

print(type(sig_name))



# for e in sig_name:
#     if( e == 'ABPmean') and (e== "Pleth"):
#         print("ABP mean exists")
#     else: 
#         print("don't exist")

if ('ABPmean'in sig_name) and ('RESP' in sig_name):
    print("exists")
else:
    print("does not")




