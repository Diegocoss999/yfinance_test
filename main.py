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
import csv
import pickle
from pytz import timezone
# pip3 install yfinance pandas matplotlibpytz
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 

#files from folder
import indicator 
import stocktest
import download
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

def get(symbol):
    d1m = download.get_1m(symbol)
    frames = [symbol,d1m]#,d2m,d1h,d1d]
    return frames


def build(frames):
    macd = indicator.macd(frames)
    print(stocktest.test("macd", macd))
    # sma_ema = indicator.sma_ema(frames)
    # stocktest.test("sma_ema", sma_ema)

# def open_folder(folder, symboltype= "*.csv"):
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
    s = "MSFT" # or ['','']
    fs = get(s)
    # build(fs)
    # plot(s)
    # test(s)

