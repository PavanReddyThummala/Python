import json
import pandas as pd
from datetime import datetime
import time
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt

# used pandas to read csv file
data = pd.read_csv (r'C:\Users\thumm\Desktop\Lesson6_Data_Stocks.csv')   
df = pd.DataFrame(data, columns= ['SYMBOL','NO_SHARES'])
print (df)

# reading json file 
file_path= 'C:/Users/thumm/Desktop/AllStocks.json'
with open(file_path) as x:
    y = json.load(x)
    #for stocks in y:
    #print(stocks['Symbol'], stocks['Date'], stocks['Open'], stocks['High'], stocks['Low'], stocks['Close'], stocks['Volume'])

class shares:
    def __int__(self,noshares, stockName):
        self.noshares=noshares
        self.stockName = stockName

class stock:
    def __init__(self,Symbol,Date,Open,High,Low,Close,Volume):
        self.Symbol=Symbol
        self.Date=Date
        self.open=Open
        self.high=High
        self.Low=Low
        self.Close=Close
        self.Volume=Volume
        
    def add_newstock(self,closingprice):
        self.closingprice=closingprice

    def calclosingprice(self, noshares):
        closep = round ((int (self.Close)) * int (noshares),2)
        return closep

Dictionary=[]
for s in y:
        if s['Symbol'].upper() not in Dictionary: 
            Dictionary.append(stock(s['Symbol'], s['Date'],s['Open'], s['High'], s['Low'], s['Close'], s['Volume']))            

#PLOTTING THE GRAPH
plot = {}
for stock in Dictionary:
    stock.add_newstock(stock.calclosingprice(df.loc[df['SYMBOL'] == stock.Symbol, 'NO_SHARES'].iloc[0]))
    if stock.Symbol.upper() not in plot:
        plot[stock.Symbol.upper()]=[]
    plot[stock.Symbol.upper()].append([datetime.strptime(stock.Date, '%d-%b-%y').strftime('%d-%m-%y'),stock.closingprice])
print(plot)
count=0
fig, ax = plt.subplots()

ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=11))
ax.xaxis.set_tick_params(rotation = 80) 
left = dt.date(2015, 11, 9)
right = dt.date(2018,11,10)
plt.gca().set_xbound(left,right)
for index, row in df.iterrows():
    xAxis = [value[0] for value in plot[row[0]]]
    yAxis = [value[1] for value in plot[row[0]]]
    ax.plot(xAxis,yAxis,)
    count=count+1
 
plt.xlabel('date')# PRINTS x-LABEL ATTRIBUTE NAME
plt.gca().invert_xaxis()
plt.ylabel('volume')# PRINTS Y-LABEL ATTRIBUTE NAME
ax.legend(list(df.SYMBOL))# PRINTS SYMBOL NAMES ON GRAPH
plt.show()
plt.savefig('WEEK8OP.png')

