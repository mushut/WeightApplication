import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def saveWeight(data):
    print("Input filename:")
    filename = input()
    with open (filename, 'w', newline='') as csvfile:
        weigthWriter = csv.writer(csvfile)
        for element in data:
            weigthWriter.writerow([element[0]] + [element[1]])

def addWeight():
    print("Date:")
    date = input()
    print("Weight:")
    weight = input()
    datapoint = (date,weight)
    return datapoint

def printWeight(data):
    time = np.arange(1,len(data)+1)
    weight = np.arange(1,len(data)+1)
    index = 0
    for element in data:
        weight[index] = float(element[1])
        index += 1

    fig, ax = plt.subplots()
    ax.plot(time,weight)

    ax.set(xlabel='Day', ylabel='Weight',title='Weight plot')
    ax.grid()

    plt.show()

def main():
    weightData = []
    print("Weight application")

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
            print("Load")
            weightData = loadWeight()

        elif choice == 2:
            print("Save")
            saveWeight(weightData)

        elif choice == 3:
            weightData.append(addWeight())

        elif choice == 4:
            print("Print weight data")
            printWeight(weightData)

        elif choice == 5:
            break

main()