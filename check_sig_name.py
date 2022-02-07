import wfdb 

def check_sig_name(path):
	signal, fields = wfdb.rdsamp(path, channel_names= ['ABP','PLETH'], warn_empty=False)  
	if fields !=None:
		sig_name= fields["sig_name"]
		if sig_name != None:
			#print(sig_name, path)
			response = 1
			# if ('ABP' in sig_name) and ('PLETH' in sig_name):
			# 	response=1
			# 	return response
			#else:
			#    pass
		else:
			response =0
	else:
		response =0
	return response
