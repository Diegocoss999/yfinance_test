'''Test stock preformance'''
import indicator
import download

file_types = ['1m','2m','1h','1d']

'''
strat['macd'] = [df['1m','2m','1h','1d'], df, df, df]
'''
def stock_test(symbol, frame):
    f1 = indicator.build(symbol, frame)
    print('positive returns are 1.0 or greater')
    for strat in list(f1.keys()):
        for interval in list(f1[strat].keys()):
            st = str(interval)+' interval performance = '+ str(run(strat, interval,f1[strat][interval]))
            print(st)
def run(strat, type, lis):
    initial = 10000
    money = initial
    percent = 0
    holdings = 0

    if strat == 'macd':
        close = lis['Close']
        e1e2 = lis['ema 12-26']
        e3 = lis['ema 9']
        # print(lis[0])
        sell_order = False
        for i in range(len(close)):
            # print(e1e2[i],' - ',e3[i])
            if e1e2[i]>=e3[i] and money >=0 and sell_order:
                #buy
                sell_order = False
                money, holdings = buy(money, close[i])
            elif e1e2[i]<e3[i]:
                #sell
                sell_order = True
                if holdings !=0:
                    money, holdings = sell(holdings, close[i])
    if strat =='gaussian':
        pass


    if holdings != 0:
        money, holdings = sell(holdings, close[i])
    percent = money / initial
    return percent *100

def buy(money, price):
    remaining = 0
    can_buy =int(money/ price)
    remaining = money - can_buy*price
    return [remaining, can_buy]

def sell(number, price):
    return [number*price, 0]

# def test_macd():
#         """12e1-26e2 > 9e3 == Buy"""
