import wfdb
from functions_preprocessing import plot

with open('/Users/itzelavila/Documents/PhD/mimicdb-1/noflatlines.txt') as f:
    signals_list = f.readlines()

print(len(signals_list))
for i in range(900,915):
    path= str.rstrip(signals_list[i])
    signal, fields = wfdb.rdsamp(path,channel_names= ['ABP','PLETH'])   
    ABP = signal[:,0]
    PLETH = signal[:,1]
    plot(ABP,'ABP',fields['fs'],path)
    plot(PLETH,'PPG',fields['fs'],path)