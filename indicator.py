"""Different stock selling strategies"""
import pandas as pd
import numpy as np
import calculator
import download

file_types = ['1m','2m','1h','1d']
def macd(s, type, frame):
    '''df['ema 12-26'], df['ema 9']'''
    e1 = 12
    e2 = 26 
    e3 = 9
    p4 = 12
    """12e1-26e2 > 9e3 == Buy"""
    df = frame.copy()

    ma_close = calculator.moving_average(df['Close'],p4)
    ema_12 = calculator.ema(df['Close'],e1,ma_close)
    ema_26 = calculator.ema(df['Close'],e2,ma_close)
    df['ema '+str(e1)+'-'+str(e2)] =list( np.array(ema_12) - np.array(ema_26 ))
    ma_ema_12_ema_26 = calculator.moving_average(df['ema '+str(e1)+'-'+str(e2)], e3 )
    df['ema '+str(e3)] = calculator.ema(df['ema '+str(e1)+'-'+str(e2)] , e3, ma_ema_12_ema_26)
    #save
    df['Chart'] = dict()
    df['Chart']['ema '+str(e1)+'-'+str(e2)] = df['ema '+str(e1)+'-'+str(e2)]
    df['Chart']['ema '+str(e3)] = df['ema '+str(e3)]
    download.save(df,s+"_"+type+"_macd")
    return df
# TODO
def sma_short_long(s, type,frame):
    short = 10
    lon = 50
    df = frame.copy()
    df['sma short'] = calculator.moving_average(df['Close'],short)
    df['sma long'] = calculator.moving_average(df['Close'],lon)

    df['Chart'] = dict()
    df['Chart']['sma short'] = df['sma short']
    df['Chart']['sma long'] = df['sma long']
    download.save(df,s+"_"+type+"_sma_short_long")
    return df

def sma_ema(s, type,frame):
    sma = 5
    ema = 20
    df = frame.copy()
    df['sma'] = calculator.moving_average(df['Close'],sma)
    df['ema'] = calculator.ema(df['Close'],ema,df['sma'])

    df['Chart'] = dict()
    df['Chart']['sma'] = df['sma']
    df['Chart']['ema'] = df['ema']
    download.save(df,s+"_"+type+"_sma_ema")
    return df
# TODO gaussian 
'''
strat['macd'] = [df,df,df,df]
'''
def build(s, frames):
    strat = dict()
    m  = dict()

    for i in range(len(frames)):

        m[file_types[i]] = macd(s, file_types[i], frames[file_types[i]])
    strat['macd'] = m
    m  =dict()
    for i in range(len(frames)):
    
        m[file_types[i]] = sma_short_long(s, file_types[i], frames[file_types[i]])
    strat['sma short long'] = m
    
    m  =dict()
    for i in range(len(frames)):
    
        m[file_types[i]] = sma_ema(s, file_types[i], frames[file_types[i]])
    strat['sma ema'] = m
    # sma_ema = indicator.sma_ema(frames)
    return strat