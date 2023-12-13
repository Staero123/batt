import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
Flight_log = {}
dirpath = r"C:\Users\AIRSHOW\Desktop\DroPort Logs\LogsCharger 20230523_20231105 CSV"
for path in os.listdir(dirpath):
    try:
        n=path[0:58]
        Flight_log[n] = pd.read_csv("/Users/AIRSHOW/Desktop/DroPort Logs/LogsCharger 20230523_20231105 CSV/"+n+'.txt.csv',sep=",",skiprows=3)
    except:
        pass

