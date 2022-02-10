
import numpy as np
import wfdb 

from functions_preprocessing import update_nan_values

with open('/Users/itzelavila/Documents/PhDMedicalDevices/Python/mimicdb-1/ABP_PLETH.txt') as f:
    signals_list = f.readlines()
f.close()

#print(len(signals_list))
'''
ex_signal=[float('nan'), float('nan'),float('nan'), float('nan'),1.2,234,5,8,2,4,6,float('nan'), float('nan'),7,4,3,4,3,4,5,7,8,9,5,4,3,2,2, float('nan')]
print(ex_signal)
ex_signal=update_nan_values(ex_signal)
print(ex_signal)'''


for i in range(100):
    path= str.rstrip(signals_list[i])
    #record= wfdb.rdrecord(path,channel_names= ['ABP','PLETH'])
    #wfdb.plot_wfdb(record=record, title='Example signals')
    signal, fields = wfdb.rdsamp(path,channel_names= ['ABP','PLETH']) 
    #print(signal[:,0])
    #print(signal[:,1])
    #print(fields['fs'])    
    ABP = signal[:,0]
    PLETH = signal[:,1]
    ABP = update_nan_values(ABP)
    PLETH = update_nan_values(PLETH)

