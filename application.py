import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

import personWeight

# Function for loading csv data from a file
def loadWeight():
    data = []
    print("Input filename")
    filename = input()
    with open(filename, newline='') as csvfile:
        weightReader = csv.reader(csvfile, delimiter=',')
        for row in weightReader:
            element = (row[0],row[1])
            data.append(element)

    return data

# Function for saving csv data to a file
def saveWeight(data):
    print("Input filename:")
    filename = input()
    with open (filename, 'w', newline='') as csvfile:
        weigthWriter = csv.writer(csvfile)
        for element in data:
            weigthWriter.writerow([element[0]] + [element[1]])

# Function for adding weight data point
def addWeight():
    print("Date (format: xx.yy.zzzz):")
    date = input()
    print("Weight:")
    weight = input()
    datapoint = (date,weight)
    return datapoint

# Printing will be moved class personWeight.
# Function for printing data as a graph
def printWeight(data):
    # Date
    # Remember that data may not be in order!
    first_date = data[0][0]
    last_date = data[-1][0]
    first_day, first_month, first_year = first_date.split('.')
    last_day, last_month, last_year = last_date.split('.')
    days1 = date(int(last_year),int(last_month), int(last_day))
    days0 = date(int(first_year),int(first_month),int(first_day))
    total_days = days0 - days1
    difference_in_days = total_days.days
    date_results = np.arange(1,difference_in_days)

    dates = np.zeros((len(data),),dtype=int)
    index_dates = 0
    for element in data:
        day, month, year = element[0].split('.')
        date_element = date(int(year),int(month),int(day))
        days = date_element - days0
        dates[index_dates] = days.days
        index_dates += 1

    # Weight
    weight = np.arange(1,len(data)+1)
    index = 0
    for element in data:
        weight[index] = float(element[1])
        index += 1

    fig, ax = plt.subplots()
    ax.plot(dates,weight)

    ax.set(xlabel='Day', ylabel='Weight',title='Weight plot')
    ax.grid()

    plt.show()

def main():
    person = personWeight.personWeight('', [])
    weightData = []
    print("Weight application")
    print("Give your user ID:")
    userID = input()
    person.setUserID(userID)

    while(True):
        print("Menu")
        print("1: Load weight data")
        print("2: Save weight data")
        print("3: Add weight data")
        print("4: Print weight data")
        print("5: Quit")

        choice_str = input()
        choice = int(choice_str)

        if choice == 1:
            # Needs to be updated
            # userID loaded from file
            print("Load")
            weightData = loadWeight()

        elif choice == 2:
            # Needs to be updated
            # userID written to file
            print("Save")
            saveWeight(weightData)

        elif choice == 3:
            print("Date (format xx.yy.zzzz):")
            date = input()
            print("Weight:")
            weight = input()
            person.addWeight(date,weight)

        elif choice == 4:
            print("Print weight data")
            person.printWeightData()

        elif choice == 5:
            break

main()