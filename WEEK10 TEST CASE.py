import unittest
from WK10Assign import Stock as Stock
class StockTestCase(unittest.TestCase):
    def test_stock_symbol(self):
        res = Stock('AIG','4-AUG-17',66.17,66.23,64.79,65.08,5074352)
        stockSymbol = res.Symbol
        self.assertEqual(stockSymbol,'AIG')
        
    def test_stock_symbol1(self):
        res = Stock('GOOGLE')
        stockSymbol = res.Symbol
        self.assertEqual(stockSymbol,'GOOG')

if __name__ == '__main__':
	unittest.main()
