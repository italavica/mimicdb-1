import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb



record = wfdb.rdrecord("/Users/itzelavila/Documents/PhDMedicalDevices/Databases/physionet.org/files/mimicdb/1.0.0/037/037n")

#wfdb.plot_wfdb(record=record, title='Example signals')
