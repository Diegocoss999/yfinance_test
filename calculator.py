'''These methods take in a list of values and return a calculated list'''
import numpy as np
import pandas as pd
import statistics


def moving_average(li, N):
    cumsum, moving_aves = [0], []

    for i, x in enumerate(li, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
        else:  
            #can do stuff with moving_ave here
            moving_aves.append((cumsum[i] - cumsum[0])/i)
    moving_aves = np.round(moving_aves, decimals=3)
    return moving_aves

'''s is list, n is period, ma is moving average'''
def ema(s,n, ma):
    """
    returns an n period exponential moving average for
    the time series s
    s is a list ordered from oldest (index 0) to most
    recent (index -1)
    n is an integer
    returns a numeric array of the exponential
    moving average
    """
    ema = []
    j = 1
    #get n sma first and calculate the next n period ema
    sma = sum(s[:n]) / n
    multiplier = 2 / float(1 + n)
    ema.append(sma)
    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(( (s[n] - sma) * multiplier) + sma)
    #now calculate the rest of the values
    for i in s[n+1:]:
        tmp = ( (i - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)
    ema = list(ma[0:n-1]) + list(ema)
    
    return list(ema)
# TODO Alex
# statistics.stdev(A_rank)
def stdev(s_list, period):
    pass
''' Some data
Open,High,Low,Close,Volume
186.7,186.85,186.7,186.85,0
186.7,186.82,186.65,186.82,0
186.99,186.99,186.99,186.99,0
186.65,186.65,186.65,186.65,0
186.76,186.76,186.6,186.6,0
186.6,186.6,186.6,186.6,0
186.79,186.79,186.67,186.67,0
186.9,186.9,186.9,186.9,0
'''

open = [186.7,186.7,186.99,186.65,186.76,186.6,186.79,186.9]
high = [186.85,186.82,186.99,186.65,186.76,186.6,186.79,186.9] # not really using
low = [186.7,186.65,186.99,186.65,186.6,186.6,186.67,186.9] # not really using
Close = [186.85,186.82,186.99,186.65,186.6,186.6,186.67,186.9]
Volume = [0,0,0,0, 0,0,0,0]



test = [10,9,8,7,6,5,4,3,2,1]
ma = list(moving_average(test,5))
# print(ma)
# print(ema(test ,3 ,ma))