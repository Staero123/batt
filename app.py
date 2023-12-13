import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
Flight_log = {}
dirpath = "C:\Users\AIRSHOW\Desktop\DroPort LogsLogs\Charger 20230523_20231105 CSV\\"
for path in os.listdir(dirpath):
    j=n[:-20]
    Flight_log[j] = pd.read_csv("/Users/AIRSHOW/Desktop/New folder/"+path+'/'+x,sep=",",skiprows=3)


