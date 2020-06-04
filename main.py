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

if __name__ == "__main__":
    s = "MSFT" # or ['','']
    frame = download.update_files(s)
    stocktest.stock_test(s,frame)
