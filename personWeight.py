import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Class for weight data
class personWeight(object):
    # Constructor
    def __init__(self, newUserID, newWeightData):
        self.userID = newUserID
        self.weightData = newWeightData

    def getWeightData(self):
        return self.weightData

    def setWeightData(self, newWeightData):
        self.weightData = newWeightData

    def getUserID(self):
        return self.userID

    def setUserID(self, newUserID):
        self.userID = newUserID

    # Add date and weight to weightData
    def addWeight(self, newDate, newWeight):
        newData = (newDate, newWeight)
        self.weightData.append(newData)

        # Reorder weightData
        # TBD

    def printWeightData(self):
        # Graphs are printed from here

        # Data for weight graph
        first_date = self.weightData[0][0]
        first_day, first_month, first_year = first_date.split('.')
        days0 = date(int(first_year), int(first_month), int(first_day))
        time_weight = np.zeros((len(self.weightData),),dtype=int)
        index_dates = 0
        for element in self.weightData:
            day, month, year = element[0].split('.')
            date_element = date(int(year), int(month), int(day))
            days = date_element - days0
            time_weight[index_dates] = days.days
            index_dates += 1

        weight = np.arange(1, len(self.weightData) + 1)
        index = 0
        for element in self.weightData:
            weight[index] = float(element[1])
            index += 1

        # Data for 7 day moving average graph
        # time_average = 0
        # weight_average = 0

        # plt.plot(time_weight, weight, 'b.-', time_average, weight_average, 'gv-')
        plt.plot(time_weight, weight, 'b.-')
        plt.show()