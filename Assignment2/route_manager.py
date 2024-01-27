#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: STUDENT_ID
"""

import sys
import yaml
import csv
import matplotlib.pyplot as plt

def sample_function(input: str) -> str:
    """Sample function (removable) that illustrations good use of documentation.
            Parameters
            ----------
                input : str, required
                    The input message.

            Returns
            -------
                str
                    The text returned.
    """
    return input.upper()

def inputFix(inp: str) -> list[str]:
    """
        This function gets the input string and creates a list and put all the important parts of the input in a list and returns it.
            Parameters
            ----------
                inp: str
                    The entire line of input.

            Returns
            -------
                list[str]
                    a list of string, each index containing one of the elements of the input file.
    """
    qcnt = False
    s = ""
    for i in range(len(inp)):
        if qcnt:
            s += inp[i]
        if inp[i] == '=':
            qcnt = True
            if i == len(inp) - 1:
                s = s[0: -1]
    return s

def airlineFix(airlines: dict()) -> dict():
    """
        This function gets the airlines file and creates dictionary mapping the details of each airline to its id.
            Parameters
            ----------
                airlines: dict()
                    The loaded yaml file of airlines.

            Returns
            -------
                dict()
                    a dictionary mapping all airline elements to its id
    """
    airlineList = []
    airlineIDList = []
    for i in range(len(airlines["airlines"])):
        airlineIDList.append(airlines["airlines"][i]["airline_id"].lstrip())
        airlineList.append({"name": airlines["airlines"][i]["airline_name"].lstrip(), "icao": airlines["airlines"][i]["airline_icao_unique_code"].lstrip(), "country": airlines["airlines"][i]["airline_country"].lstrip()})
    airlinesInfo = dict(zip(airlineIDList, airlineList))
    return airlinesInfo

def airportFix(airports: dict()) -> dict():
    """
        This function gets the airports file and creates dictionary mapping the details of each airport to its id.
            Parameters
            ----------
                airport: dict()
                    The loaded yaml file of airports.

            Returns
            -------
                dict()
                    a dictionary mapping all airport elements to its id
    """

    airportList = []
    airportIDList = []
    for i in range(len(airports["airports"])):
        airportIDList.append(airports["airports"][i]["airport_id"].lstrip())
        airportList.append({"name": airports["airports"][i]["airport_name"].lstrip(), "city": airports["airports"][i]["airport_city"].lstrip(), "country": airports["airports"][i]["airport_country"].lstrip(), "icao": airports["airports"][i]["airport_icao_unique_code"].lstrip(), "altitude": airports["airports"][i]["airport_altitude"].lstrip()})
    airportsInfo = dict(zip(airportIDList, airportList))
    return airportsInfo
    
def routeFix(routes: dict()) -> dict():
    """
        This function gets the routes file and creates a list of dictionaries each containing the details of a route.

            Parameters
            ----------
                routes: dict()
                    The loaded yaml file of airlines.

            Returns
            -------
                dict()
                    a list of dictionaries containing all of the routes information
    """

    routeList = []
    for i in range(len(routes["routes"])):
        routeList.append({"airline_id": routes["routes"][i]["route_airline_id"].lstrip(), "from": routes["routes"][i]["route_from_aiport_id"].lstrip(), "to": routes["routes"][i]["route_to_airport_id"].lstrip()})
    return routeList


def solveQ1(airlinesInfo: dict(), airportsInfo: dict(), routesInfo: list[dict()], graphType: str) -> None:
    """
        This function solves the 1st question. it creates a new dictionary and counts for each airline how many flights they have had to Canada.
        Then it sorts the data in ascending order, and it will cut it to contain only the first 15 elements.
        Finally, it will write the data in a csv file and will call the appropriate function to create the graph.
            
            Parameters
            ----------
                airlinesInfo: dict()
                    The dictionary containing airlines information.
                airportsInfo: dict()
                    The dictionary containing airports information.
                routesInfo: dict()
                    The dictionary containing routes information.
                graphType: str
                    The string that outlines what sort of graph should be created for this question.
                
            Returns
            -------
                Nothing.

    """
    cnt = dict()
    for i in range(len(routesInfo)):
        if routesInfo[i]["to"] in airportsInfo:
            if airportsInfo[routesInfo[i]["to"]]["country"] == "Canada":
                if routesInfo[i]["airline_id"] in cnt:
                    cnt[routesInfo[i]["airline_id"]] += 1
                else:
                    cnt[routesInfo[i]["airline_id"]] = 1
    result = dict()
    for i in cnt:
        if i in airlinesInfo:
            tmp = str(airlinesInfo[i]["name"] + " (" + airlinesInfo[i]["icao"] + ")")
            result[tmp] = cnt[i]
    result = dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))
    result = dict(list(result.items())[0:20])

    with open("q1.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "statistic"])
        row = []
        for i in result:
            row.append([i, result[i]])
        writer.writerows(row)

    if graphType == "bar":
        barGraph(result, "Top 15 airlines with most flights to Canada", "Airlines", "Number of Flights", "q1.pdf")

    if graphType == "pie":
        pieGraph(result, "Top 15 airlines with most flights to Canada", "q1.pdf")



def solveQ2(airportsInfo: dict(), routesInfo: dict(), graphType: str) -> None:
    """
        This function solves the 2nd question. it creates a new dictionary and counts how many flights landed in each country.
        Then it sorts the data in ascending order, and it will cut it to contain only the first 30 elements.
        Finally, it will write the data in a csv file and will call the appropriate function to create the graph.
            
            Parameters
            ----------
                airportsInfo: dict()
                    The dictionary containing airports information.
                routesInfo: dict()
                    The dictionary containing routes information.
                graphType: str
                    The string that outlines what sort of graph should be created for this question.
                
            Returns
            -------
                Nothing.

    """

    cnt = dict()
    for i in range(len(routesInfo)):
        if (routesInfo[i]["to"] in airportsInfo):
            routesInfo[i]["to"].lstrip()
            if (airportsInfo[routesInfo[i]["to"]]["country"] in cnt):
                cnt[airportsInfo[routesInfo[i]["to"]]["country"]] += 1
            else:
                cnt[airportsInfo[routesInfo[i]["to"]]["country"]] = 1
    cnt = dict(sorted(cnt.items(), key = lambda x: (x[1], x[0])))
    cnt = dict(list(cnt.items())[0:30])
    with open("q2.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "statistic"])
        for i in cnt:
            writer.writerow([i, cnt[i]])

    if graphType == "bar":
        barGraph(cnt, "The 30 country with least flight to them", "Countries", "Number of Flights", "q2.pdf")

    if graphType == "pie":
        pieGraph(cnt, "Top 15 airlines with most flights to Canada", "q2.pdf")



def solveQ3(airportsInfo: dict(), routesInfo: dict(), graphType: str) -> None:
    """
        This function solves the 3rd question. it creates a new dictionary and counts how many flights landed in each airport.
        Then it sorts the data in descending order, and it will cut it to contain only the first 10 elements.
        Finally, it will write the data in a csv file and will call the appropriate function to create the graph.
            
            Parameters
            ----------
                airportsInfo: dict()
                    The dictionary containing airports information.
                routesInfo: dict()
                    The dictionary containing routes information.
                graphType: str
                    The string that outlines what sort of graph should be created for this question.
                
            Returns
            -------
                Nothing.

    """

    cnt = dict()
    for i in range(len(routesInfo)):
        if (routesInfo[i]["to"] in airportsInfo):
            if (routesInfo[i]["to"] in cnt):
                cnt[routesInfo[i]["to"]] += 1
            else:
                cnt[routesInfo[i]["to"]] = 1

    result = dict()
    for i in cnt:
        tmp = airportsInfo[i]["name"] + " (" + airportsInfo[i]["icao"] + "), " + airportsInfo[i]["city"] + ", " + airportsInfo[i]["country"]
        result[tmp] = cnt[i]

    result = dict(sorted(result.items(), key = lambda x: (-x[1], x[0])))
    result = dict(list(result.items())[0:10])
    with open("q3.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "statistic"])
        for i in result:
            writer.writerow([i, result[i]])

    if graphType == "bar":
        barGraph(result, "Top 10 airports with most flights to them", "Airport Name", "Number of Flight", "q3.pdf")

    if graphType == "pie":
        pieGraph(result, "Top 15 airlines with most flights to Canada", "q3.pdf")

def solveQ4(airportsInfo: dict(), routesInfo: dict(), graphType: str) -> None:
    """
        This function solves the 4th question. it creates a new dictionary and counts how many flights landed in each city.
        Then it sorts the data in descending order, and it will cut it to contain only the first 10 elements.
        Finally, it will write the data in a csv file and will call the appropriate function to create the graph.
            
            Parameters
            ----------
                airportsInfo: dict()
                    The dictionary containing airports information.
                routesInfo: dict()
                    The dictionary containing routes information.
                graphType: str
                    The string that outlines what sort of graph should be created for this question.
                
            Returns
            -------
                Nothing.

    """

    cnt = dict()
    for i in range(len(routesInfo)):
        if (routesInfo[i]["to"] in airportsInfo):
            tmp = airportsInfo[routesInfo[i]["to"]]["city"] + ", " + airportsInfo[routesInfo[i]["to"]]["country"]
            if (tmp in cnt):
                cnt[tmp] += 1
            else:
                cnt[tmp] = 1
    cnt = dict(sorted(cnt.items(), key = lambda x: (x[1], x[0]), reverse = True))
    cnt = dict(list(cnt.items())[0:15])
    with open("q4.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "statistic"])
        for i in cnt:
            writer.writerow([i, cnt[i]])

    if graphType == "bar":
        barGraph(cnt, "Top 10 Cities with most flights to them", "City", "Number Of Flights", "q4.pdf")
            
    if graphType == "pie":
        pieGraph(cnt, "Top 15 airlines with most flights to Canada", "q4.pdf")

def solveQ5(airportsInfo: dict(), routesInfo: dict(), graphType: str) -> None:
    """
        This function solves the 5th question. it creates a new dictionary, putting for each unique route, the altitude between the two airports.
        Then it sorts the data in descending order, and it will cut it to contain only the first 10 elements.
        Finally, it will write the data in a csv file and will call the appropriate function to create the graph.
            
            Parameters
            ----------
                airportsInfo: dict()
                    The dictionary containing airports information.
                routesInfo: dict()
                    The dictionary containing routes information.
                graphType: str
                    The string that outlines what sort of graph should be created for this question.
                
            Returns
            -------
                Nothing.

    """

    cnt = dict()
    for i in range(len(routesInfo)):
        if (routesInfo[i]["from"] in airportsInfo) and (routesInfo[i]["to"] in airportsInfo) and (airportsInfo[routesInfo[i]["from"]]["country"] == "Canada") and (airportsInfo[routesInfo[i]["to"]]["country"] == "Canada"):
            tmp1 = airportsInfo[routesInfo[i]["from"]]["icao"]
            tmp2 = airportsInfo[routesInfo[i]["to"]]["icao"]
            dif = abs(float(airportsInfo[routesInfo[i]["from"]]["altitude"]) - float(airportsInfo[routesInfo[i]["to"]]["altitude"]))
            r1 = tmp1 + "-" + tmp2
            r2 = tmp2 + "-" + tmp1
            if (r1 in cnt):
                cnt[r1] = max(dif, cnt[r1])
            elif (r2 in cnt):
                if (dif >= cnt[r2]):
                    cnt.pop(r2)
                    cnt[r1] = dif
            else:
                cnt[r1] = dif
    cnt = dict(sorted(cnt.items(), key = lambda x: (x[1], x[0]), reverse = True))
    cnt = dict(list(cnt.items())[0:10])
    with open("q5.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "statistic"])
        for i in cnt:
            writer.writerow([i, cnt[i]])


    if graphType == "bar":
        barGraph(cnt, "Top 10 unique Canadian routes with biggest altitude difference", "Routes", "altitude Difference", "q5.pdf")

    if graphType == "pie":
        pieGraph(cnt, "Top 15 airlines with most flights to Canada", "q5.pdf")



def barGraph(data: dict(), pTitle: str, xTitle: str, yTitle: str, question: str) -> None:
    """
        This function gets the datas and created a bar graph represnting the data.

            Parameters
            ----------
                data: dict()
                    The dictionary containing the datas that are to be shown on the graph.
                xTitle: str
                    The title for the x-axis.
                yTitle: str
                    The title for the y-axis.
                pTitle: str
                    The title for the graph.

            Returns
            -------
                Nothing.

"""
    x_label = []
    y_label = []
    for i in data:
        x_label.append(i)
        y_label.append(data[i])
    plt.bar(x_label, y_label)
    plt.title(pTitle, fontsize=10)
    plt.xticks(fontsize=1, rotation=45)
    plt.yticks(fontsize=5)
    plt.xlabel(xTitle, fontsize=4)
    plt.ylabel(yTitle, fontsize=4)
    plt.savefig(question)


def pieGraph(data: dict(), pTitle: str, question: str) -> None:
    """
        This function gets the datas and created a pie graph represnting the data.

            Parameters
            ----------
                data: dict()
                    The dictionary containing the datas that are to be shown on the graph.
                axisTitle: str
                    The title for the datas in pie graph.
                pTitle: str
                    The title for the graph.

            Returns
            -------
                Nothing.

    """

    plt.rcParams['font.size'] = 5
    dataValues = []
    dataLabels = []
    for i in data:
        dataValues.append(data[i])
        dataLabels.append(i)
    plt.pie(dataValues, labels = dataLabels, autopct = '%1.1f%%', textprops={'fontsize': 3})
    plt.title(pTitle, fontsize=12, color='red')
    plt.savefig(question)


def solve(airlinesInfo: dict(), airportsInfo: dict(), routesInfo: dict(), graphType: str, question: str) -> None:
    """
        This function gets the question type and calls the functions appropriate to solve each question.

            Parameters
            ----------
                question: str
                    question type.

            Returns
            -------
                Nothing.
    """

    if question == "q1":
        solveQ1(airlinesInfo, airportsInfo, routesInfo, graphType)
    if question == "q2":
        solveQ2(airportsInfo, routesInfo, graphType)
    if question == "q3":
        solveQ3(airportsInfo, routesInfo, graphType)
    if question == "q4":
        solveQ4(airportsInfo, routesInfo, graphType)
    if question == "q5":
        solveQ5(airportsInfo, routesInfo, graphType)



def main():
    """Main entry point of the program."""
    """
        This part of the code takes the input and read the files specified by the input.
    """
    sys.argv[1] = inputFix(sys.argv[1])
    sys.argv[2] = inputFix(sys.argv[2])
    sys.argv[3] = inputFix(sys.argv[3])
    sys.argv[4] = inputFix(sys.argv[4])
    sys.argv[5] = inputFix(sys.argv[5])
    with open(sys.argv[1], 'r') as file:
        airlines = yaml.safe_load(file)
    with open(sys.argv[2], 'r') as file:
        airports = yaml.safe_load(file)
    with open(sys.argv[3], 'r') as file:
        routes = yaml.safe_load(file)

    question = sys.argv[4]
    graphType = sys.argv[5]
    airlinesInfo = airlineFix(airlines)
    airportsInfo = airportFix(airports)
    routesInfo = routeFix(routes)

    """
        This part of the code passes the input data to a function to solve it.
    """
    solve(airlinesInfo, airportsInfo, routesInfo, graphType, question)


if __name__ == '__main__':
    main()
