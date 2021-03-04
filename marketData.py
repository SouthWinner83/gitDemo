import datetime
import numpy as np

import quantUtils

class Context:
    def __init__(self,asOfDate, spot, vol, rates = 0.0):
        if type(asOfDate) is not datetime.date:
            raise ValueError('As-of-Date should be a date')
        self.asOfDate = asOfDate
        self.spot = spot
        self.vol = vol
        self.rates = rates
        
    def forward(self,date):
        if type(date) is not datetime.date:
            raise ValueError('date should be a date')
        if (date < self.asOfDate):
            raise ValueError('the date should be after as of date')
        timeToMat = quantUtils.timeDifference(self.asOfDate, date)
        result = self.spot * np.exp(self.rates * timeToMat)
        return result


