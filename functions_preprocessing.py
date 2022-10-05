from operator import truediv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from math import sqrt
from matplotlib import pyplot
import pandas as pd


def update_nan_values(signal):
    len_signal=len(signal)
    signal_has_nan = np.isnan(signal)
    nan = 0
    nn=0
    
    #check if the entire signal is nan
    for s in signal_has_nan:
        if s:
            nn=nn+1
    if nn>= len_signal/2:
        for i in range(len_signal):
            signal[i]=0
    else:
        for i in range(len_signal):
            if i==0:
                if signal_has_nan[i]:
                    nan+=1
                    c=i
                    while signal_has_nan[c]:
                        c+=1
                    signal[i]= signal[i+c]

            elif (i>0) and (i<(len_signal-1)):
                if signal_has_nan[i]:
                    nan+=1
                    c=i
                    while signal_has_nan[c]:
                        c+=1
                        if c == len_signal:
                            break
                        signal[i]= signal[i-1]
                        

            elif (i == len_signal-1):
                if signal_has_nan[i]:
                    nan+=1
                    signal[i]= signal[i-1]
    # print("Nan= ", nan)
    return signal

signal = np.array([1,1,1,2,3,4,5,6,7,float('nan'),float('nan'),float('nan'),8,8,8,8,8,8,98,1,5,3,57,7,2,2,5,1,1,34,7,3,3,3,3,3,3,3])
signal = update_nan_values(signal)
#print(signal)
df=pd.read_feather('/Users/itzelavila/Documents/PhD/mimicdb-1/mimic_filtered.ftr')
PLETH=df['PLETH']




def flat_lines_check(signal):
    len_signal=len(signal)
    x=0
    i=0
    countX=0
    seg=[0]
    numElm=2
    for e in signal:
        if e == x:
            #recta horizontal
            countX+=1
        elif (e!=x) and (countX>0):
            seg.append(countX)
            countX=0
        
        else:
            countX=0
        #print("signal:", len(signal)-1)
        if i == (len(signal)-1) and countX>0:
            seg.append(countX)
        x=e
        i+=1
    return seg





def remove_flat_records(signal1,signal2, path,fl,nfl):
    seg1=flat_lines_check(signal1)
    seg2=flat_lines_check(signal2)
    # print((max(seg1)>5) or (max(seg2)>5))
    # print(path)
    if (max(seg1)>5) or (max(seg2)>5):
        with open('flatlines.txt', 'a') as fl:
            fl.write(path + "\n")
    elif (max(seg1)<5) or (max(seg2)<5):
        with open('noflatlines.txt', 'a') as nfl:
            nfl.write(path + "\n")




def check_ABP(ABP):
    r= False
    for i in range(len(ABP)):
        if ABP[i] >300 or ABP[i]<15:
            r= True
        elif r==False: 
            r=False
        elif r==True:
            r=True
    return r

def check_PPG(PPG):
    lensignal=len(PPG)
    dPPG=[]
    g0=[]
    g=0
    l=0
    rg=False
    rl=False
    l0=[]

    dPPG=np.diff(PPG)
    # plot(PPG,'PPG',125,'')
    # plot(dPPG,'dPPG',125,'')
    # print(len(dPPG))
    # print(dPPG)
    for i in range(lensignal-1):
        if dPPG[i]>0:
            g0.append(1)
        else:
            g0.append(0)
    for i in range(lensignal-1):
        if dPPG[i]<0:
            l0.append(1)
        else:
            l0.append(0)

    for i in range(len(g0)-2):
        if g0[i]==1 and g0[i+1]==1:
            if g>=170:
                rg= True
            g=g+1
        else:
            g=0
    if rg != True and g <170:
        rg= False
    
    for i in range(len(l0)-2):
        if l0[i]==1 and l0[i+1]==1:
            if l>=170:
                rl= True
            l=l+1
        else:
            l=0
    if rl != True and l <170:
        rl= False
    return rg+rl
        
            


        
    
    

        




def plot(signal,signal_name,fs,path):
    L= len(signal)
    signal_time = np.arange(0, L/fs, 1/fs)
    plt.figure()
    plt.plot(signal_time,signal, label=signal_name)
    plt.title(signal_name +' ' + path[-8:])
    plt.xlabel('Time (s)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()




def normalize(ABP):

    L=len(ABP)
        #concatenate all rows in one
    ABP_values= np.concatenate(ABP)
    
    # ABP_values_splitted=np.split(ABP_values,n)

    #prepare data for normalization
    ABP_values=ABP_values.reshape((len(ABP_values),1))

    #train the normalization
    scaler = MinMaxScaler(feature_range=(0,1))
    scaler = scaler.fit(ABP_values)
    print('Min: %f, Max: %f' %(scaler.data_min_,scaler.data_max_))

    #normalize ABP values and print 5 rows
    value_normalized= scaler.transform(ABP_values)

    # ABP_values=ABP_values.reshape((1,len(ABP_values)))
    # value_normalized=value_normalized.reshape((1,len(value_normalized)))
  
    ABP=value_normalized.reshape(1,len(value_normalized))
    ABP=np.split(ABP[0],754)
    return ABP

def standardize(PLETH):
    L=len(PLETH)

    PLETH=np.concatenate(PLETH)
    
    # PLETH_series=pd.Series(PLETH)
    # PLETH_series.hist()
    # pyplot.show()

    #prepare data for standardization
    PLETH=PLETH.reshape((len(PLETH),1))

    #train the standardization
    scaler= StandardScaler()
    scaler =scaler.fit(PLETH)
    print('Mean: %f, StandardDEviation: %f' %(scaler.mean_,sqrt(scaler.var_)))

    #standardization of PLETH values
    standardised= scaler.transform(PLETH)
    PLETH=standardised.reshape(1,len(standardised))
    PLETH=np.split(PLETH[0],754)




    
    # PLETH=[]
    # for i in standardised:
    #     i=i.reshape((1,len(i)))
    #     PLETH.append(i)
    

    return PLETH




""" #normalization ABP
ABP_normalized=[]
ABP_normalized_inversed=[]
for value in df['ABP'].values:

    #prepare data for normalization
    value=value.reshape((len(value),1))
    print(len(value))

    #train the normalization
    scaler = MinMaxScaler(feature_range=(0,1))
    scaler = scaler.fit(value)
    print('Min: %f, Max: %f' %(scaler.data_min_,scaler.data_max_))

    #normalize ABP values and print 5 rows
    value_normalized= scaler.transform(value)
    ABP_normalized.append(value_normalized)

    #inverse transform
    value_normalized_inversed= scaler.inverse_transform(value_normalized)
    ABP_normalized_inversed.append(value_normalized_inversed)

for i in range(5):
    print(ABP_normalized[i])


for i in range(5):
    print(ABP_normalized_inversed[i]) """