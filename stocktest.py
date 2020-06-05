'''Test stock preformance'''
import indicator
import download
import plot
file_types = ['1m','2m','1h','1d']

'''
strat['macd'] = [df['1m','2m','1h','1d'], df, df, df]
'''
def stock_test(symbol, frame):
    df = indicator.build(symbol, frame)
    print('positive returns are 1.0 or greater')
    for strat in list(df.keys()):
        for interval in list(df[strat].keys()):
            st = strat+' ' + str(interval)+' interval performance = '+ str(run(strat, interval,df[strat][interval]))
            print(st)
    plot.gui(df)
def run(strat, type, df):
    initial = 10000
    money = initial
    percent = 0
    holdings = 0
    close = df['Close']
    df['Performance'] = list()
    if strat == 'macd':
        del df['Open']
        del df['Volume']
        del df['High']
        del df['Low']
        e1e2 = df['ema 12-26']
        e3 = df['ema 9']
        sell_order = False
        for i in range(len(close)):
            if e1e2[i] <= e3[i] and money >=0 and sell_order:
                #buy
                sell_order = False
                money, holdings = buy(money, close[i])
            elif e1e2[i] > e3[i]:
                #sell
                sell_order = True
                if holdings !=0:
                    money, holdings = sell(holdings, close[i])
            df['Performance'].append(money)
        '''clean up '''

    if strat =='gaussian':
        pass
    if strat =='sma short long':
        del df['Open']
        del df['Volume']
        del df['High']
        del df['Low']
        sma_short = df['sma short']
        sma_long = df['sma long']
        sell_order = False
        for i in range(len(close)):
            if sma_long[i] >= sma_short[i] and money >=0 and sell_order:
                #buy
                sell_order = False
                money, holdings = buy(money, close[i])
            elif sma_long[i] < sma_short[i]:
                #sell
                sell_order = True
                if holdings !=0:
                    money, holdings = sell(holdings, close[i])
            df['Performance'].append(money)
    if strat =='sma ema':
        del df['Open']
        del df['Volume']
        del df['High']
        del df['Low']
        sma = df['sma']
        ema = df['ema']
        sell_order = False
        for i in range(len(close)):
            if ema[i] >= sma[i] and money >=0 and sell_order:
                #buy
                sell_order = False
                money, holdings = buy(money, close[i])
            elif ema[i] < sma[i]:
                #sell
                sell_order = True
                if holdings !=0:
                    money, holdings = sell(holdings, close[i])
            df['Performance'].append(money)
    # final money count
    if holdings != 0:
        money, holdings = sell(holdings, close[-1])
    percent = money / initial
    return percent 

def buy(money, price):
    remaining = 0
    can_buy =int(money/ price)
    remaining = money - can_buy*price
    return [remaining, can_buy]

def sell(number, price):
    return [number*price, 0]

# def test_macd():
#         """12e1-26e2 > 9e3 == Buy"""
