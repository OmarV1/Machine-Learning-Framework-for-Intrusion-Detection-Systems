import numpy as np
import pandas as pd 
import pickle 
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
import os

GB = 'GB_MODEL_PKL'
GB_model = pickle.load(open(GB, 'rb')) # loading the binary .pkl

if len(sys.argv) == 1:
    print('no argument given')
else:
    path = sys.argv[1]
    if os.path.exists(path):
        
        test = pd.read_csv(path)
        test = test.iloc[::,::]
        
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
                
        test  = test[newx]
            

        print('########### Binary classification is loading #############')


        result1 = GB_model.predict(test) # lunch predication 

        print(result1)

        print('......Binary classfication result......')

        for i in result1:
            if i == 1:
                print('Attack traffic!!')
            else:
                print('Benign')

        pred = pd.DataFrame(result1, columns = ['pred']) # convert array to pandas
        test['n_pred'] = pred 
        test = test.loc[test['n_pred'] != 0] # eliminate all benign traffic 

        print('########### Multiclass classification is loading #############')
        GB_model = pickle.load(open("GB_MULTI_PKL", 'rb'))
        test = test.iloc[::,:-1]
        result = GB_model.predict(test)
        print(result)


        #print(".......Muliclass attack is loading.....")

        for i in result :
            if i == 1:
                print('DDOS attack-HOIC')
            elif i == 2:
                print('DDoS attacks-LOIC-HTTP')
            elif i == 3 :
                print('DoS attacks-Hulk')
            elif i == 4:
                print('Bot')
            elif i == 5:
                print ('FTP-BruteForce')
            elif i == 6 :
                print('SSH-Bruteforce')
            elif i == 7 :
                print('Infilteration')
            elif i == 8 :
                print ('DoS attacks-SlowHTTPTest')
            elif i == 9 :
                print('DoS attacks-GoldenEye')
            elif i == 10:
                print('DoS attacks-Slowloris')
            elif i == 11:
                print ('DDOS attack-LOIC-UDP')
            elif i == 12 :
                print('Brute Force -Web')
            elif i == 13 :
                print('Brute Force -XSS')
            elif i == 14 :
                print('SQL Injection')
