import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("StudentsPerformance.csv")
possibleDataEntries= ["gender","race/ethnicity","parental level of education","lunch","test preparation course"]

def getAverages():
    avg = []
    for i in range(len(file.index)):
        scores = file.iloc[i, 5:8]
        avg.append(sum(scores/3).round())
    return avg

def xAndData(dataToAcc):
    fileLoc = file[dataToAcc]
    avgs = getAverages()
    studentList = [[] for _ in range(len(avgs))]

    cont = 0
    while cont < len(avgs):
        for i in fileLoc:
            studentList[cont].extend([i, avgs[cont]])
            cont+=1
    
    return studentList

def avgAvgsLmao(data):
    countDict = {}
    avgsDict = {}

    for i in range(len(data)):
        if data[i][0] in countDict.keys():
            countDict[data[i][0]] += 1
        else:
            countDict[data[i][0]] = 1

        if data[i][0] in avgsDict.keys():
            avgsDict[data[i][0]] += data[i][1]
        else:
            avgsDict[data[i][0]] = data[i][1]

    for i in avgsDict.keys():
        avgsDict[i] = (avgsDict[i]/countDict[i]).round()

    return avgsDict

# print(avgAvgsLmao(xAndData("race/ethnicity")))

def graphIt(data, selctedOut):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('dark_background')

    _, ax = plt.subplots()
    ax.bar(list(data.keys()), list(data.values()))
    ax.set_xticklabels(list(data.keys()), rotation=60, horizontalalignment="right", fontsize=10)
    ax.set_title(f"Average Scores By {selctedOut} (Averaging Math, Reading, & Writing)", fontsize=15)
    ax.set_ylabel("Average Scores")
    ax.set_xlabel(f"{selctedOut}")
    plt.show()

def userChoice():
    user = input("Access What Data [type: ['help', '?'] to bring up help menu]: ")

    if user in ["help", "?"]:
        print("\nList Of Possible Entries:")
        print(possibleDataEntries, "\n")
        

    elif user in possibleDataEntries:
        print("pog")
        dat = xAndData(user)
        avg = avgAvgsLmao(dat)
        graphIt(avg, user)

    userChoice()

if __name__ == "__main__":
    userChoice()