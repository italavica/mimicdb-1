import numpy as np



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
