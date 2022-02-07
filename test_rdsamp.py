import wfdb
import os 
with open('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/RECORDS') as f:
    lines = f.readlines()
f.close()
i=0
 
path_dat= '/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/474n' + ".dat" 
if os.path.exists(path_dat):
#signal, fields = wfdb.rdsamp('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/474', channel_names= ['ABP','PLETH'])  
	signal,fields = wfdb.rdsamp('/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/474/474n', channel_names=['ABP','PLETH'], warn_empty=True)
			
	print(fields)
else:
	print('not exists')