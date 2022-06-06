"""
Name : Pavan Kumar Thummala
Date : 05/8/2022
Purpose : Stock Problem by importing CSV Files
"""

import datetime
import csv
class Stock:
    def __init__ (self, stocksymbol, shares , purchaseValue, currentValue, purchaseDate):
        self.stocksymbol = stocksymbol
        self.shares = shares
        self.purchaseValue = purchaseValue
        self.currentValue = currentValue
        self.purchaseDate = purchaseDate

    def Interval(self):
        from datetime import datetime
        currentDate= datetime.now()
        previous= self.purchaseDate
        #previous = date.fromisoformat(previous)
        totaldays = ((currentDate - previous).days)
        return totaldays
    
    def earningorLoss(self):
        earningLoss = round(((self.currentValue) - (self.purchaseValue))*(self.shares),2)
        return earningLoss
    
    def yearlyearningloss(self):
        yrEarningRate = round((((((self.currentValue) - (self.purchaseValue))/self.purchaseValue)/(Stock.Interval(self))) * 100), 4) 
        return yrEarningRate
    
    def Stocktable(self):
        print ("{:<12}".format(self.stocksymbol),"{:<12}".format(self.shares),"{:<14}".format(self.purchaseValue),"{:<14}".format(self.currentValue),(self.purchaseDate.strftime('%m-%d-%Y')),file=f)

    def yrtable(self):
        print("{:<12}".format(self.stocksymbol),"{:<12}".format(self.shares),"{:<12}".format(Stock.earningorLoss(self)),"{:<12}".format(Stock.yearlyearningloss(self)), file = f)

class Bond:
    def __init__(self, stocksymbol, Shares , purchaseValue, currentValue, purchaseDate, coupon, bondYield):
        self.stocksymbol = stocksymbol
        self.Shares = Shares
        self.purchaseValue = purchaseValue
        self.currentValue = currentValue
        self.purchaseDate = purchaseDate
        self.coupon = coupon       
        self.bondYield= bondYield
        
    def Bonddetails(self):
        try:
            with open("bondsfile.txt", "a") as f:
                print("{:<12}".format(self.stocksymbol),"{:<10}".format(self.Shares),"{:<14}".format(self.purchaseValue),"{:<14}".format(self.currentValue),"{:<14}".format(self.purchaseDate.strftime('%m-%d-%Y')),"{:<14}".format(self.coupon),"{:<12}".format(self.bondYield),file =f)
        except:
            raise Exception('unable to write to file')

stock = []
with open('C:\\Users\\thumm\\Desktop\\Lesson6_Data_Stocks.csv','r') as file:
    try:
        try:
            reader = csv.reader(file)
        except :
            raise FileNotFoundError("The "+ filename + "does not exist.")
        for row in list(reader)[1:]:
            if type(row[0]) == str:
                stockSymbol = row[0]
            else:
                raise TypeError(row[0],' is not string type')
            try:
                 shares=int(row[1])
            except TypeError:
                raise TypeError(row[1]," is not int type")
            try:
                 purchaseValue=float(row[2])
            except TypeError:
                raise TypeError(row[2]," is not float type")
            try:
                 currentValue=float(row[3])
            except TypeError:
                raise TypeError(row[3]," is not float type")
            try:
                 purchaseDate = datetime.datetime.strptime(row[4], '%m/%d/%Y')
            except ValueError:
                raise ValueError(row[4],"Incorrect data format, should be MM-DD-YYYY")
            stock.append(Stock(stockSymbol,shares,purchaseValue,currentValue,purchaseDate))
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
print("successfully executed")

bonds = []
with open('C:\\Users\\thumm\\Desktop\\Lesson6_Data_Bonds.csv','r') as file:
    reader = csv.reader(file)
    for row in list(reader)[1:]:
        if type(row[0]) == str:
            stockSymbol = row[0]
        else:
            raise TypeError(row[0],' is not string type')
        try:
             shares=int(row[1])
        except TypeError:
            raise TypeError(row[1], " is not int type")
        try:
             purchaseValue=float(row[2])
        except TypeError:
            raise TypeError(row[2]," is not float type")
        try:
             currentValue=float(row[3])
        except TypeError:
            raise TypeError(row[3]," is not float type")
        try:
             purchaseDate = datetime.datetime.strptime(row[4], '%m/%d/%Y')
        except ValueError:
            raise ValueError(row[4],"Incorrect data format, should be MM-DD-YYYY")
        try:
             coupon=float(row[5])
        except TypeError:
            raise TypeError(row[5]," is not float type")
        try:
             bondYield=float(row[6])
        except TypeError:
            raise TypeError(row[6]," is not float type")
        bonds.append(Bond(stockSymbol,shares,purchaseValue,currentValue,purchaseDate,coupon, bondYield))
        
#Prints bondtable in File1
with open("bondsfile.txt","a") as f:
    print('\n\n\t\t\tBond Ownership for BOB SMITH', file =f)
    print('_'*90,file=f)
    print("{:<12}".format("stocksymbol"),"{:<10}".format("Shares"),"{:<14}".format("purchaseValue"),"{:<14}".format("currentValue"),"{:<14}".format("purchaseDate"),"{:<14}".format("coupon"),"{:<12}".format("bondYield"),file =f)
    print('_'*90,file=f)
bonds[0].Bonddetails()

#Prints stocktable in File2        
with open("stocktablefile.txt","a") as f:
    print('_'*80, file =f)
    print("{:<10}".format("STOCK"),"{:<12}".format("SHARES"),"{:<14}".format("PURCHASEVALUE"),"{:<14}".format("CURRENTVALUE"),"{:<14}".format("PURCHASEDATE"),file=f)
    print('_'*80,file=f)
    for i in stock:
        i.Stocktable()

#Prints earninglosstable in File2  
with open("stocktablefile.txt","a") as f:
    print('_'*80, file =f)
    print("{:<10}".format("STOCK"),"{:<12}".format("SHARES"),"{:<14}".format("earningorloss"),"{:<14}".format("yearlyearningloss"),file=f)
    print('_'*80,file=f)
    for i in stock:
        i.yrtable()       
