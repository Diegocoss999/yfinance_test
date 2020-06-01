#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/yfinance
# Dataframe Notes: df.iloc[0]['A']
"""
Sanity check for most common library uses all working

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Index: S&P500
- Currency BTC-USD
"""

from __future__ import print_function
import yfinance as yf
import datetime
from datetime import timedelta
import pandas as pd
import pandas_datareader as pdr
import glob
import os
from pathlib import Path
# import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import matplotlib
# matplotlib.use("TkAgg")
# if True:
#     from matplotlib.figure import Figure
#     from matplotlib import *
#     from matplotlib.backends import *
#     from matplotlib.backends.backend_tkagg import *

import indicator 
import stocktest

         
def get_1m(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    file = 'data/'+symbol+"_1m.csv"
    df = pd.DataFrame()
    try: # if exists append
        # TODO
        df = pd.read_csv(file)
        s = df.iloc[-1]["Datetime"].split('-')
        # if datetime.date(int(s[0]),int(s[1]),int(s[2].split(' ')[0])) != datetime.date.today():
        #     df2 = df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        #     df = pd.concat([df,df2]).drop_duplicates()
    except(FileNotFoundError ): # create new
        # print("error")
        df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
    # df.to_csv(file)
    return df

def get_2m(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    file = 'data/'+symbol+"_2m.csv"
    df = None
    try: # if exists append
        df = pd.read_csv(file)
        # df2 = df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        # df = pd.concat([df,df2]).drop_duplicates()
    except(FileNotFoundError): # create new
        df = yf.download(symbol,interval = "2m", start=end- timedelta(days=29,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
    # df.to_csv(file)
    return df
def get_1h(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    file = 'data/'+symbol+"_1h.csv"
    df = None
    try: # if exists append
        # TODO
        df = pd.read_csv(file)
        # df2 = df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        # df = pd.concat([df,df2]).drop_duplicates()
        # print(df)
    except(FileNotFoundError): # create new
        df = yf.download(symbol,interval = "1h", start=end- timedelta(days=729,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
    # df.to_csv(file)
    return df
def get_1d(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    file = 'data/'+symbol+"_1d.csv"
    df = None
    try: # if exists append
        # TODO
        df = pd.read_csv(file)
        # df2 = df = yf.download(symbol,interval = "1m", start=end- timedelta(days=6,minutes=59), end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        # df = pd.concat([df,df2]).drop_duplicates()
    except(FileNotFoundError): # create new
        df = yf.download(symbol,interval = "1d", start=start, end=end,auto_adjust = True, prepost = True,threads = False,   proxy = "PROXY_SERVER" )

    # df.to_csv(file)
    return df

def get(symbol,start=datetime.datetime(1,1,1), end=datetime.date.today()):
    d1m = get_1m(symbol)
    d2m = get_2m(symbol)
    d1h = get_1h(symbol)
    d1d = get_1d(symbol)
    '''process'''
    frames = [symbol,d1m,d2m,d1h,d1d]
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
    build(fs)
    plot(s)
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