from check_sig_name import check_sig_name
import os

def check_signal(path):
    path_dat= path + ".dat" 
    if os.path.exists(path_dat):
        response = check_sig_name(path)
     
    else:
        response = 0

    return response 
