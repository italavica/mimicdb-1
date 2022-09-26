
import numpy as np
import wfdb 
from tqdm import tqdm

from functions_preprocessing import flat_lines_check, update_nan_values,plot,remove_flat_records

path_records='/Users/itzelavila/Documents/PhD/mimicdb-1/records_raw.txt'
path_database='/Users/itzelavila/Documents/PhD/databases/mimic-database-1.0.0'
with open(path_records) as f:
    signals_list = f.readlines()
f.close()
nfl= open('noflatlines.txt', 'w')
fl= open('flatlines.txt', 'w')
#print(len(signals_list))
'''
ex_signal=[float('nan'), float('nan'),float('nan'), float('nan'),1.2,234,5,8,2,4,6,float('nan'), float('nan'),7,4,3,4,3,4,5,7,8,9,5,4,3,2,2, float('nan')]
print(ex_signal)
ex_signal=update_nan_values(ex_signal)
print(ex_signal)'''


for i in tqdm(signals_list):
    path= path_database+str.rstrip(i)
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
    #plot(ABP,'ABP',fields['fs'],path)
    #plot(PLETH,'PPG',fields['fs'],path)
    remove_flat_records(ABP,PLETH, path,fl,nfl)
nfl.close()
fl.close()
