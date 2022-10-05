
import pandas as pd
import numpy as np
import feather
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from math import sqrt
from matplotlib import pyplot
from functions_preprocessing import check_PPG, update_nan_values, flat_lines_check,normalize,standardize
from tqdm import tqdm

df=pd.read_feather('/Users/itzelavila/Documents/PhD/mimicdb-1/mimic_filtered.ftr')

""" #Preprocess ABP and PPG signals
#update nan values
PLETH=[]
for signal in tqdm(df['PLETH']):
    signal=update_nan_values(signal)
    PLETH.append(signal)

ABP=[]
for signal in tqdm(df['ABP']):
    signal=update_nan_values(signal)
    ABP.append(signal)

#flat lines check  #check PPG
PLETHS=[]
ABPS=[]
for i in tqdm(range(len(ABP))):
    seg1=flat_lines_check(ABP[i])
    seg2=flat_lines_check(PLETH[i])
    diff=check_PPG(PLETH[i])
    if (max(seg1)<5) and (max(seg2)<5) and diff==0:
         PLETHS.append(PLETH[i])
         ABPS.append(ABP[i])

#convert to pd.Series
PLETHS=pd.Series(PLETHS)
ABPS=pd.Series(ABPS)

df2=pd.DataFrame(np.transpose(PLETHS),columns=['PLETH'])
df2.insert(loc=1,column='ABP', value=ABPS)
#Save to feather format
df2.to_feather('./mimic_flat_lineschecked.ftr')
         """
#Standardization PPG and normalization ABP
df1=pd.read_feather('/Users/itzelavila/Documents/PhD/mimicdb-1/mimic_flat_lineschecked.ftr')


ABP=normalize(df1['ABP'])
PLETH=standardize(df1['PLETH'])

#convert to pd.Series
PLETH=pd.Series(PLETH)
ABP=pd.Series(ABP)

df3=pd.DataFrame(np.transpose(PLETH),columns=['PLETH'])
df3.insert(loc=1,column='ABP', value=ABP)
#Save to feather format
df3.to_feather('./mimic_preprocessed.ftr')

















