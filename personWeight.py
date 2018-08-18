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