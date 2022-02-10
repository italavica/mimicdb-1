import wfdb
from functions_preprocessing import plot

with open('/Users/itzelavila/Documents/PhDMedicalDevices/Python/mimicdb-1/flatlines.txt') as f:
    signals_list = f.readlines()

for e in signals_list:
    path= str.rstrip(e)
    signal, fields = wfdb.rdsamp(path,channel_names= ['ABP','PLETH'])   
    ABP = signal[:,0]
    PLETH = signal[:,1]
    plot(ABP,'ABP',fields['fs'],path)
    plot(PLETH,'PPG',fields['fs'],path)