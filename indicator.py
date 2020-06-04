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
    download.save(df,s+"_"+type+"_macd")
    return df
# TODO
def sma_ema(frames):
    pass
    # p1 = 5
    # p2 = 20
    # p3 = 10
    # df = frames[1].copy()
    # # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # '''short term sma'''
    # ma_close = calculator.moving_average(df['Close'],p3)
    # df['moving average '+str(p1)] = calculator.moving_average(df['Close'],p1)
    # df['moving average '+str(p3)] = calculator.moving_average(df['Close'],p3)
    # df['moving average '+str(p2)] = calculator.moving_average(df['Close'],p2)
    # df['moving average '+str(p3)] = calculator.ema(df,p3,ma_close)
    # #save
    # df.to_csv('data/'+frames[0]+"_1m_sma-ema.csv")
    # return [df['Datetime'], df['Close'], df['moving average '+str(p1)], df['moving average '+str(p3)], df['moving average '+str(p2)], df['moving average '+str(p3)] ]
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
    # sma_ema = indicator.sma_ema(frames)
    return strat