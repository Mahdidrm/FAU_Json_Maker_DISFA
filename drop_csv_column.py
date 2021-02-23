# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:58:47 2021

@author: mehdi
"""
import datetime
import xlrd            
import pandas as pd
f=pd.read_csv("D:/XAI/Code/OpenFace_2.2.0_win_x64/processed/csv.csv")
keep_col = ['frame',
            ' x_1',' x_8', ' x_15',' x_18', ' x_21', ' x_22', ' x_25',' x_27',' x_28',' x_31',' x_35',' x_37',' x_38',
            ' x_41', ' x_43',' x_44',' x_46', ' x_48',' x_51',' x_54', ' x_57',' x_62',' x_66',
            
            
            ' y_1',' y_8', ' y_15',' y_18', ' y_21', ' y_22', ' y_25', ' y_27',' y_28',' y_31',' y_35', ' y_37',' y_38',
            ' y_41', ' y_43', ' y_44',' y_46',' y_48', ' y_51',' y_54', ' y_57',' y_62',' y_66',
            
            ' AU01_r', ' AU02_r', ' AU04_r', ' AU05_r', ' AU06_r', ' AU09_r',' AU12_r', ' AU15_r', ' AU17_r', ' AU20_r', 
            ' AU25_r', ' AU26_r']

new_f = f[keep_col]

new_f2 = new_f[['frame',
                 ' x_21', ' y_21',' AU01_r',' x_22',' y_22',' AU01_r',                           #The corner of the eyebrows near to nose
                 ' x_18', ' y_18',' AU02_r',' x_25',' y_25',' AU02_r',                           #The highest point of the eyebrows
                 ' x_27',' y_27',' AU04_r',                                                      #Between the eyebrows
                 ' x_37', ' x_38',' y_37',' y_38',' AU05_r',' x_43',' x_44',' y_43',' y_44',' AU05_r',   #Above the eyelids
                 ' x_1',' x_31',' x_41', ' y_1',' y_31',' y_41',' AU06_r',' x_15',' x_46',' x_35',' y_15',' y_46',' y_35',' AU06_r',    #Cheek Raiser
                 ' x_31', ' y_31',' AU09_r',' x_35',' y_35',' AU09_r', ' x_28',' y_28',' AU09_r',    
                 ' x_48', ' y_48',' AU12_r',' x_54',' y_54',' AU12_r',
                 ' x_48', ' y_48',' AU15_r',' x_54',' y_54',' AU15_r',
                 ' x_57',  ' y_57',' AU17_r',' x_8', ' y_8',' AU17_r', 
                 ' x_51', ' y_51',' AU20_r', ' x_51', ' y_51',' AU20_r',
                 ' x_62', ' y_62',' AU25_r',' x_66', ' y_66',' AU25_r',
                 ' x_62', ' y_62',' AU26_r',' x_66', ' y_66',' AU26_r' ]] # rearrange as you like

new_f2.to_csv("D:/XAI/Code/OpenFace_2.2.0_win_x64/processed/DISFA_NEW.csv", index=False)

