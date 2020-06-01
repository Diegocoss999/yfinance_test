import numpy as np
# def moving_average_10(li,N=10):
#     return li.Series(x).rolling(window=N).mean().iloc[N-1:].values
def moving_average(li, N):
    cumsum, moving_aves = [0], []

    for i, x in enumerate(li, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
        else:
            temp = N
            
            moving_ave = (cumsum[i] - cumsum[0])/i
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    moving_aves = np.round(moving_aves, decimals=3)
    return moving_aves
import pandas as pd

def ema(f, period):
    data = f['Close'].ewm(span=period).mean()
    data.head(period)
    data = np.round(data, decimals=3)
    # print(data)
    
    data.iloc[0:period] = f[0:period]['ma']
    f.head(20)
    return data
def ema_2(s,n, ma):
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
    #
    print(ma[0:n-1])
    print(ema)
    ema = list(ma[0:n-1]) + list(ema)
    
    return list(ema)

test = [10,9,8,7,6,5,4,3,2,1]
ma = list(moving_average(test,5))
# print(ma)
# print(ema_2(test ,3 ,ma))