'''Test stock preformance'''
# pip3 install yfinance pandas matplotlibpytz
def test(type, lis):
    initial = 10000
    money = 10000
    # goal = 7 #%
    percent = 0
    holdings = 0

    if type == 'macd':
        """12e1-26e2 > 9e3 == Buy"""
        close = lis[1]
        e1e2 = lis[2]
        e3 = lis[3]
        # print(lis[0])
        for i in range(len(lis[0])):
            # print(e1e2[i],' - ',e3[i])
            if e1e2[i]>=e3[i] and money >=0 :
                #buy
                money, holdings = buy(money, close[i])
            elif e1e2[i]<e3[i]:
                #sell
                if holdings !=0:
                    money, holdings = sell(holdings, close[i])
    if type =='gaussian':
        pass
    percent = money / initial
    return percent

def buy(money, price):
    remaining = 0
    can_buy =int(money/ price)
    remaining = money - can_buy*price
    return [remaining, can_buy]

def sell(number, price):
    return [number*price, 0]

