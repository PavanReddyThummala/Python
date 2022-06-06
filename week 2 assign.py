"""
Name : Pavan Kumar Reddy Thummala
Date : 04/10/2022
This Program prints the bob's highest increase in value on a per share basis
"""

import sys #sys provides various variables and functions used to manipulate different parts of python
stocks = ["GOOGLE", "MSFT","RDS-A", "AIG","FB"]
numOfShares = [25,85,400,235,130]
purchasePrice = [772.88,56.60,49.58,54.21,124.31]
currentValue = [941.53,73.04,55.74,65.27,175.45]

#prints the above given list in a tabular form

print("stocks\t\tNo.Shares\tpurchasePrice\tcurrentValue")
for i in range(len(stocks)):
    print(stocks[i],numOfShares[i],purchasePrice[i],currentValue[i],sep="\t\t")
print("----------")

print("\tStock ownership for Bob Smith")#prints the header of Output
print("stock\t\tShares#\t\tEarnigs/Loss")

maxStock=- sys.maxsize-1
resultantStock=''
for i in range(len(stocks)):
    print(f'{stocks[i]}\t\t{numOfShares[i]}\t\t${(numOfShares[i]*(currentValue[i]-purchasePrice[i])):.2f}')
    if maxStock < (currentValue[i]-purchasePrice[i]):
        maxStock=currentValue[i]-purchasePrice[i]
        resultantStock=stocks[i]
#prints the share value that highest increase or least decrese
if maxStock > 0:
    print("The stock with the highest increase in value in your portfolio on a per-share basis is:"f'{resultantStock}')
else:
    print("The stock with the least decrease in value in your portfolio on a per-share basis is:"f'{resultantStock}')



