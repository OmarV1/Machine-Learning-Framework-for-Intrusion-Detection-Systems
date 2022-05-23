import numpy as np
import pandas as pd 
import pickle 
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import os
import subprocess
from threading import Timer
from time import sleep 

GB = 'GB_MODEL_PKL'
GB_model = pickle.load(open(GB, 'rb')) # loading the binary .pkl

#os.system("cicflowmeter -i eth0 -c test.csv")

#p = subprocess.Popen( 'cicflowmeter -i eth0  -c  test.csv',shell = True)
#try:
 #   p.wait(10)
#except subprocess.TimeoutExpired:
 #   p.kill()
    
    
    
#if len(sys.argv) == 1:
#    print('no argument given')
#else:
#    path = sys.argv[1]
#    if os.path.exists(path):
newx= ['protocol'
,'flow_duration'
,'tot_fwd_pkts'
,'tot_bwd_pkts'
,'totlen_fwd_pkts'
, 'totlen_bwd_pkts'
,'fwd_pkt_len_mean'
,'fwd_pkt_len_std'
,'bwd_pkt_len_mean'
,'flow_byts_s'
,'flow_pkts_s'
,'flow_iat_std'
,'flow_iat_min'
,'fwd_iat_tot'
,'fwd_iat_min'
, 'bwd_iat_tot'
,'bwd_iat_min'
,'fwd_psh_flags'
,'fwd_urg_flags'
,'bwd_pkts_s'
,'fin_flag_cnt'
, 'rst_flag_cnt'
,'psh_flag_cnt'
,'ack_flag_cnt'
,'urg_flag_cnt'
,'down_up_ratio'
,'init_fwd_win_byts'
,'init_bwd_win_byts'
,'fwd_seg_size_min'
,'active_mean' ,'idle_mean']
 
GB = 'GB_MODEL_PKL'
GB_model = pickle.load(open(GB, 'rb')) # loading the binary .pkl       
counter = 0

while True :
    try:
        for row in pd.read_csv('flow.csv', chunksize=1):
            row = row[newx]
            result = GB_model.predict(row)
            sleep(0.5)
            result1 = GB_model.predict(row) # lunch predication 
            #print(result1)
            for i in result1:
                if i == 1:
                    print('Attack traffic!!')
                else:
                    print('Benign')
    except:
        sleep(1)
        print('waiting for new traffic')
        continue