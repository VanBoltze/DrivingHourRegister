path = "0"


def storeNewEP(date, length, car):
    dataset = open(path, mode="a+")
    stringData = ";" + "\n" + date + "," + str(length) + "," + car
    dataset.write(stringData)

defaultCar = "0"

def readEP(car = defaultCar):
    exp = 0
    dataset = open(path)
    table = dataset.read()
    table = table.split(";")
    for i in range(len(table)):
        table[i] = table[i].split(",")
    for i in range(len(table)):
        if table[i][2] == car:
            exp += int(table[i][1])
    print(exp)

def getAllCars():
    carList = []
    tmp = False
    dataset = open(path)
    table = dataset.read()
    table = table.split(";")
    for i in range(len(table)):
        table[i] = table[i].split(",")
    for i in range(len(table)):
        for c in carList:
            if table[i][2] == c:
                tmp = True
        if not tmp:
            carList.append(table[i][2])
     for c in carList:
        print(c)
    
def createNewRegister(namePath):
    file = open(namePath, "w+")
    file.write("0.0.0,0,0")

use = 1
print("Type 0 to exit the program.")
while use != 0:
    order = input(path + ">>")
    if order == "readEP":
        readEP(defaultCar)
    elif order == "setCar":
        defaultCar = input("Car: ")
    elif order == "getCar":
        print(defaultCar)
    elif order == "newRegister":
        path = input("Path + Name (folders divided by double backslash): ")
        createNewRegister(path)
    elif order == "getRegister":
        print(path)
    elif order == "storeNewEP":
        storeNewEP(input("Date: "), int(input("Length in minutes: ")), input("Car: "))
    elif order == "0":
        use = 0
    elif order == "setRegister":
        path = input("File Path: ")
    elif order == "getAllCars":
        getAllCars()
    else:
        print("command not found")

