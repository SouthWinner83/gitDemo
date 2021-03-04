import marketData as marketData
import datetime
#import numpy as np



asOfDate = datetime.date(2018,5,19)  
maturity = datetime.date(2019,5,19)  
spot = 100
vol = 0.2
rates = 0.05

myContext = marketData.Context(asOfDate, spot, vol, rates)
print(myContext.forward(maturity))

