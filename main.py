#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/Diegocoss999/yfinance_test
"""
Goal: Test various stock trading strategies.

"""
# import
from __future__ import print_function
import datetime
from datetime import timedelta
import glob
import os
from pathlib import Path
# pip3 install yfinance pandas matplotlibpytz
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pytz import timezone
import csv
import pickle
#files from folder
import indicator 
import stocktest
# Planning to use
''' 
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
if True:
    from matplotlib.figure import Figure
    from matplotlib import *
    from matplotlib.backends import *
    from matplotlib.backends.backend_tkagg import *
'''   
# globals
folder = 'data/pickle/'
# dict extentions
def concat(self,d2):
    # end of self's last date
    date_str = str(self['Datetime'][-1])
    date = datetime.datetime.strptime(date_str[0:16],'%Y-%m-%d %H:%M')
    # check that d2 dates are not repeats
    for index in range(len(list(self['Datetime']))):
        date_2_str = str(d2['Datetime'][index])
        date_2 = datetime.datetime.strptime(date_2_str[0:16],'%Y-%m-%d %H:%M')
        if date < date_2: # in order dates
            # Add d2 to self
            for key in list(self.keys()):
                if key != '':
                    self[key] = list(self[key]) + list(d2[key][index:len(d2[key])])

def save(df, file):
    file = folder +file +'.pkl'
    f = open(file,"wb")
    pickle.dump(dict(df),f)
    f.close()
    # delete = True
    # for key in list(df.keys()):
    #     if key == 'Datetime':
    #         delete = False
    #     if delete:
    #         del df[key]
def read( file):
    file = folder +file +'.pkl'
    f = open(file,"rb")
    df = pickle.load(f)
    f.close()
    delete = True
    for key in list(df.keys()):
        if key == 'Datetime':
            delete = False
        if delete:
            del df[key]
    return df
def dict_fix(d):
    
    for s in list(d.keys()):
        li = list()
        for key, value in d[s].items():
            li.append(value)
        d[s] = li
def dumb_code(df, file):
    df.to_csv(file)
    df = pd.read_csv(file)
    df = df.to_dict()
    dict_fix(df)
    return df
def dict_demo():
    file = 'data/1m_test'
    d1 = {"Datetime": ['2020-05-27 04:15','2020-05-27 04:16' ],"Close": [180,181],"Open": [190,191]}
    d2 = {"Datetime": ['2020-05-27 04:16' ,'2020-05-27 04:17','2020-05-27 04:18'  ],"Close": [180,190,191],"Open": [180,200,201]}
    concat(d1, d2)
    print(d1)
    save(d1, file)
    del d1
    d1 = dict()
    d1 = read(file)
    print(d1)
def get_1m(symbol, end=datetime.datetime.now()):
    file = symbol+"_1m"
    df = pd.DataFrame()
    try: # if exists append
        # TODO
        df = read(file)
        date_str = df['Datetime'][-1][0:16]
        # 2020-05-26 19:10
        date = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M')
        end = end + timedelta(hours=3)
        end = datetime.datetime(year=end.year,month=end.month,day=end.day,hour=end.hour,minute=end.minute)
        if date < end:
            df2 = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end, auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
            df2 = dumb_code(df2, folder+'t.csv')
            concat(df,df2)
            save(df, file)
            print(df["Datetime"][-1])
    except(FileNotFoundError ): # create new
        df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        df = dumb_code(df, folder+'t.csv')
        save(df, file)
        # print(df)
    return df

# def get_2m(symbol, end=datetime.date.now(timezone('EST'))):
#     file = 'data/'+symbol+"_2m.csv"
#     return df
# def get_1h(symbol, end=datetime.date.today()):
#     file = 'data/'+symbol+"_1h.csv"
#     return df
# def get_1d(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
#     file = 'data/'+symbol+"_1d.csv"
#     return df

def get(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    d1m = get_1m(symbol)
    # d2m = get_2m(symbol)
    # d1h = get_1h(symbol)
    # d1d = get_1d(symbol)
    '''process'''
    frames = [symbol,d1m]#,d2m,d1h,d1d]
    return frames

def plot(symbol):
    try:
        d1m = pd.read_csv('data/'+symbol+"_1m_macd.csv")
        d2m= pd.read_csv('data/'+symbol+"_2m.csv")
        d1h= pd.read_csv('data/'+symbol+"_1h.csv")
        d1d = pd.read_csv('data/'+symbol+"_1d.csv")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
        """raw data"""
        plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['Close'], label='1m') # normal
        # plt.plot(d2m[1:-1]['Datetime'], d2m[1:-1]['Close'], label='2m')# normal
        # plt.plot(d1h[1:-1]['Date'], d1h[1:-1]['Close'], label='1h')# normal
        # plt.plot(d1d[1:-1]['Date'], d1d[1:-1]['Close'], label='1d') #
        """moving average"""
        # plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['moving average 10'], label='1m_av')
        l1 = 'ema 12-26'
        plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1][l1], label=l1)
        l2 = 'ema 9'
        plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1][l2], label=l2)
        """ewm"""
        # plt.plot(d1m[1:-1]['Datetime'], d1m[1:-1]['ewm 10'], label='1m_ewm_10')
        # plt.plot(days,y)
        plt.gcf().autofmt_xdate()
        plt.xlabel('Date')
        plt.ylabel('Price (open)')
        plt.title('Prediction plot')
        plt.legend()
        plt.show()
    except(FileNotFoundError):
        pass
def build(frames):
    macd = indicator.macd(frames)
    print(stocktest.test("macd", macd))
    # sma_ema = indicator.sma_ema(frames)
    # stocktest.test("sma_ema", sma_ema)
# def open_folder(folder, type= "*.csv"):
#     path_folder = Path(folder)
#     folder_search = os.path.join(path_folder, Path(type))
#     files= glob.glob(folder_search)
#     print(files)
#     return files

# def read_folder():
#     # read old downloaded data
#     for f in  open_folder("", type=s+"_7d_1m"):
#         frame = pd.read_csv(f)
#         print(frame)
#         print(frame.iloc[0]['Datetime'])

if __name__ == "__main__":
    # options:  [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    # Notes: 1hour, The requested range must be within the last 730 days.
    """
    1m 7 days
    2m 30 days
    1h 730 days
    1d max days
    """
    # test_yfinance()
    s = "MSFT" # or ['','']
    fs = get(s)
    # build(fs)
    # plot(s)
    # test(s)

# def gui():
#     root = tk.Tk()
#     root.title('Anomaly Detection')
#     root.geometry("960x540")
   
#     # graph_frame = Frame(root)
#     # graph_frame.pack()
#     # self.f = Figure(figsize=(5, 5), dpi=100)

#     # self.timeseries = self.f.add_subplot(111)

#     # self.timeseries.set_title('Events', fontsize=16)
#     # # a.set_title ("Time Series", fontsize=16)
#     # self.timeseries.set_ylabel("Number of Events", fontsize=14)
#     # self.timeseries.set_xlabel("Time (min)", fontsize=14)

#     # self.canvas = FigureCanvasTkAgg(self.f, graph_frame)
#     # self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#     # toolbar = NavigationToolbar2Tk(self.canvas, graph_frame)
#     # toolbar.update()
#     # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#     root.mainloop()