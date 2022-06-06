import sys #sys provides various variables and functions used to manipulate different parts of python
from datetime import date
today = date.today()


def profitloss(stocks):
    for i in stocks:
        x= (stocks[i][0]*(stocks[i][2] - stocks[i][1]))
        x= round(x,2)
        stocks[i].append(x)

def percentageProfitLoss(stocks):
    perval =[]
    for i in stocks:
        perval.append(((stocks[i][2]-stocks[i][1])/stocks[i][1])*100)

def yearlyProfitLoss(stocks):
    for i in stocks:
        yearDiff = today.year - int(stocks[i][3][-4:])
        x = (((((stocks[i][2] - stocks[i][1])/stocks[i][1])/yearDiff))*100)
        x= round(x,2)
        stocks[i].append(x)

stocks = {
    "GOOGLE" : [125,772.88,941.53, "8/1/2017"],
    "MSFT" : [85, 56.60,73.04,"8/1/2017"],
    "RDS-A" : [400,49.58,55.74,"8/1/2017"],
    "AIG" : [235,54.21,65.27,"8/1/2017"],
    "FB" : [130,124.31,175.45,"8/1/2017"],
    "M" : [425,30.30,23.98,"1/10/2018"],
    "F" : [85,12.58,10.95,"2/17/2018"],
    "IBM" : [80,150.37,145.30,"5/12/2018"]
    
}

yearlyProfitLoss(stocks)
profitloss(stocks)
percentageProfitLoss(stocks)


#prints the above given list in a tabular form
print("-" *65)
print("stocks\t\tNo.Shares\tEarningorloss\t yearlyEarningorloss")
print("-" *65)
k = list(stocks.keys())
j=0
for i in (stocks):
    print(k[j],stocks[i][0],stocks[i][5],stocks[i][4],sep="\t\t")
    j=j+1
print("-" *65)