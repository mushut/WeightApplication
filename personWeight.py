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
        time_weight = 0
        weight = 0

        # Data for 7 day moving average graph
        time_average = 0
        weight_average = 0

        plt.plot(time_weight, weight, 'b.-', time_average, weight_average, 'gv-')
        plt.show()