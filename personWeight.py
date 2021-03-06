import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime

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
        self.weightData = sorted(self.weightData, key=lambda element: date(element[0][2], element[0][1], element[0][0]))

    # Consider dividing printing to two functions (One for basic graph and another for 7 day moving average
    def printWeightData(self):
        # Data for weight graph
        first_date = self.weightData[0][0]
        first_day, first_month, first_year = first_date
        days0 = date(first_year, first_month, first_day)
        time_weight = np.zeros((len(self.weightData),),dtype=int)
        index_dates = 0
        for element in self.weightData:
            day = element[0][0]
            month = element[0][1]
            year = element[0][2]
            date_element = date(year,month,day)
            days = date_element - days0
            time_weight[index_dates] = days.days
            index_dates += 1

        weight = np.arange(1, len(self.weightData) + 1, dtype=float)
        index = 0
        for element in self.weightData:
            weight[index] = float(element[1])
            index += 1

        # Data for 7 day moving average graph
        # Has to be daily plot. Have to estimate daily values for weight. (Long timescale and efficiency!?)
        # One way is to have weight be as much as latest weight data is (Bad approximation)
        # Other way would be to calculate lines from weight elements and approximate daily weights from the line
        # time_average = 0
        # weight_average = 0

        # 1) Daily weight for days that have no weight data is equal to the earlier weight before date

        # Get current date
        current_date = datetime.now()

        # Generate arrays for 7 day moving average
        date_difference_average = current_date - first_date
        time_average = np.zeros((date_difference_average.days), dtype=int)
        weight_average = np.arange(1, date_difference_average.days, dtype=float)

        # Start going through dates daily
        for day_iterator in time_average:
            # Keep latest weight in variable
            # Check if there is weight for day_iterator date
            # TBD

        # plt.plot(time_weight, weight, 'b.-', time_average, weight_average, 'gv-')
        plt.plot(time_weight, weight, 'b.-')
        plt.show()