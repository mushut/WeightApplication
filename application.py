import csv

import personWeight

# Function for loading csv data from a file
def loadWeight():
    data = []
    print("Input filename")
    filename = input()
    with open(filename, newline='') as csvfile:
        weightReader = csv.reader(csvfile, delimiter=';')
        userID = next(weightReader,None)
        for row in weightReader:
            date = (row[0].split('.'))
            date_as_integers = [0,0,0]
            date_as_integers[0] = int(date[0])
            date_as_integers[1] = int(date[1])
            date_as_integers[2] = int(date[2])
            element = (date_as_integers,row[1])
            data.append(element)

    person = personWeight.personWeight(userID, data)

    return person

# Function for saving csv data to a file
def saveWeight(person):
    print("Input filename:")
    filename = input()
    with open (filename, 'w', newline='') as csvfile:
        weigthWriter = csv.writer(csvfile, delimiter=';')
        weigthWriter.writerow([person.getUserID()])
        for element in person.getWeightData():
            weigthWriter.writerow([element[0]] + [element[1]])

def main():
    person = personWeight.personWeight('', [])
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
            print("Load")
            person = loadWeight()

        elif choice == 2:
            print("Save")
            saveWeight(person)

        elif choice == 3:
            print("Date (format xx.yy.zzzz):")
            date = input()
            date_parsed = date.split('.')
            date_parsed_as_integers = [0, 0, 0]
            date_parsed_as_integers[0] = int(date_parsed[0])
            date_parsed_as_integers[1] = int(date_parsed[1])
            date_parsed_as_integers[2] = int(date_parsed[2])
            print("Weight:")
            weight = input()
            person.addWeight(date_parsed_as_integers,weight)

        elif choice == 4:
            print("Print weight data")
            person.printWeightData()

        elif choice == 5:
            break

main()