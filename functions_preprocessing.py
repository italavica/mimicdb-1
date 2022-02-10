import numpy as np
import matplotlib.pyplot as plt




def update_nan_values(signal):
    len_signal=len(signal)
    signal_has_nan = np.isnan(signal)
    nan = 0
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
    print("Nan= ", nan)
    return signal

#signal = [1,1,1,2,3,4,5,6,7,8,8,8,8,8,8,98,1,5,3,57,7,2,2,5,1,1,34,7,3,3,3,3,3,3,3]
#print(signal)

def flat_lines_check(signal):
    len_signal=len(signal)
    x=0
    i=0
    countX=0
    seg=[]
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
    print((max(seg1)>5) or (max(seg2)>5))
    print(path)
    if (max(seg1)>5) or (max(seg2)>5):
        with open('flatlines.txt', 'a') as fl:
            fl.write(path + "\n")
    elif (max(seg1)<5) or (max(seg2)<5):
        with open('noflatlines.txt', 'a') as nfl:
            nfl.write(path + "\n")

#seg=flat_lines_check(signal)
#print(seg)


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




