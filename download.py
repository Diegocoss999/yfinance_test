"""Download stock data"""
import yfinance as yf
import datetime
from datetime import timedelta
import pandas as pd
import pickle
import glob
import os
from pathlib import Path
folder = 'data/pickle/'
file_types = ['1m','2m','1h','1d']
type_dates = {'1m':timedelta(days=6, hours=23,minutes=59),'2m':timedelta(days=11, hours=23,minutes=59),'1h':timedelta(days=729),'1d':timedelta(days=2019*365)}
# def open_folder(folder,  type= "*.csv"):
#     path_folder = Path(folder)
#     folder_search = os.path.join(path_folder, Path(type))
#     files= glob.glob(folder_search)
#     print(files)
#     return files

# def read_folder():
#     type = type=s+"_7d_1m"
#     path_folder = Path(folder)
#     folder_search = os.path.join(path_folder, Path(type))
#     files= glob.glob(folder_search)
#     # read old downloaded data
#     for f in  files:
#         frame = pd.read_csv(f)
#         print(frame)
#         print(frame.iloc[0]['Datetime'])


# dict extentions
def delete(df):
    for key in list(df.keys()):
        df[key] = df[key][int(len(df[key])/2):len(df[key])]

def concat(self,d2):
    # end of self's last date
    date_str = str(self['Datetime'][-1])
    date = datetime.datetime.strptime(date_str[0:16],'%Y-%m-%d %H:%M')
    # check that d2 dates are not repeats
    for index in range(len(list(d2['Datetime']))):
        date_2_str = str(d2['Datetime'][index])
        date_2 = datetime.datetime.strptime(date_2_str[0:16],'%Y-%m-%d %H:%M')
        if date < date_2: # in order dates
            # Add d2 to self
            for key in list(self.keys()):
                if key != '':
                    self[key] = list(self[key]) + list(d2[key][index:len(d2[key])])
                    # self['Datetime'] = list(self['Datetime']) + list(d2['Datetime'][index:len(d2['Datetime'])])

            return

def save(df, file):
    file = folder +file +'.pkl'
    f = open(file,"wb")
    pickle.dump(dict(df),f)
    f.close()
def read( file):
    file = folder + file + '.pkl'
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
def update_file(symbol,interval='1m'):
    end=datetime.datetime.now()
    file = symbol+"_"+interval
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
            df2 = yf.download(symbol,start =  end - type_dates[interval], end=end+timedelta(hours=3),interval = interval, auto_adjust = False, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
            df2 = dumb_code(df2, folder+'t.csv')
            concat(df,df2)
            save(df, file)
            print(df["Datetime"][-1])
    except(FileNotFoundError ): # create new
        df = yf.download(symbol,start = end - type_dates[interval], end=end +timedelta(hours=3), interval = interval, auto_adjust = False, prepost = True,threads = False,   proxy = "PROXY_SERVER" )
        df = dumb_code(df, folder+'t.csv')
        # print(df)
        # print(df['Datetime'][-1])
        save(df, file)
        
    return df
def update_files(symbol, end=datetime.datetime.now()):
    file_types = ['1m','2m']#,'1h','1d']
    frames = dict()
    for type in file_types:
        frames[type] = update_file(symbol, type)
    return frames
