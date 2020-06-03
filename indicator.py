import pandas as pd
import numpy as np
import calculator
file_types = ['1m','2m','1h','1d']
def macd(frames):
    e1 = 12
    e2 = 26 
    e3 = 9
    p4 = 12
    """12e1-26e2 > 9e3 == Buy"""
    df = frames[1].copy()
    # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    '''short term sma'''
    # print(df)
    
    df['ma'] = calculator.moving_average(df['Close'],p4)
    df['ema '+str(e1)] = calculator.ema_2(df['Close'],e1,df['ma'])
    df['ema '+str(e2)] = calculator.ema_2(df['Close'],e2,df['ma'])
    df['ema '+str(e1)+'-'+str(e2)] = df['ema '+str(e1)] - df['ema '+str(e2)] 
    ma = calculator.moving_average(df['ema '+str(e1)+'-'+str(e2)], p4 )
    a = calculator.ema_2(df['ema '+str(e1)+'-'+str(e2)] , e3, ma)
    # print(a)
    df['ema '+str(e3)] = a
    #save
    df.to_csv('data/'+frames[0]+"_1m_macd.csv")
    return [df['Datetime'], df['Close'], df['ema '+str(e1)+'-'+str(e2)],df['ema '+str(e3)] ]
# TODO
def sma_ema(frames):
    p1 = 5
    # p2 = 20
    # p3 = 10
    # df = frames[1].copy()
    # # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # '''short term sma'''
    # df['ma'] = calculator.moving_average(df['Close'],p3)
    # df['moving average '+str(p1)] = calculator.moving_average(df['Close'],p1)
    # df['moving average '+str(p3)] = calculator.moving_average(df['Close'],p3)
    # df['moving average '+str(p2)] = calculator.moving_average(df['Close'],p2)
    # df['moving average '+str(p3)] = calculator.ema_2(df,p3,df['ma'])
    # #save
    # df.to_csv('data/'+frames[0]+"_1m_sma-ema.csv")
    # return [df['Datetime'], df['Close'], df['moving average '+str(p1)], df['moving average '+str(p3)], df['moving average '+str(p2)], df['moving average '+str(p3)] ]
# TODO gaussian 
