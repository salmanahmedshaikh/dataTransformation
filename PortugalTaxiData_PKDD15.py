import csv
import ast
import math

from geojson import Point, Feature
from datetime import datetime

def extractData():

    inputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/data.csv"
    outputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/transformedTrajData.csv"

    # Attributes: TRIP_ID, CALL_TYPE, ORIGIN_CALL, ORIGIN_STAND, TAXI_ID, TIMESTAMP, DAYTYPE, MISSING_DATA, POLYLINE
    # "1372808091620000624","C","","","20000624","1372808091","A","False","[[-8.606448,41.14467],[-8.607033,41.144859],[-8.607717,41.143743],[-8.608158,41.143185],[-8.608185,41.142924],[-8.606016,41.142402],[-8.605179,41.143437],[-8.604585,41.144661],[-8.604378,41.145075],[-8.603838,41.145381],[-8.603496,41.145489],[-8.602137,41.145624],[-8.600427,41.145768],[-8.600418,41.146884],[-8.599221,41.147847],[-8.599059,41.147973],[-8.598681,41.148252],[-8.598672,41.148234],[-8.598663,41.148225],[-8.598762,41.149071],[-8.597682,41.151042],[-8.596377,41.15331],[-8.596332,41.153598],[-8.596458,41.153733],[-8.597205,41.15403],[-8.597934,41.154372],[-8.59896,41.154678],[-8.598762,41.155533],[-8.59851,41.155866],[-8.598366,41.156397],[-8.598411,41.156496],[-8.598582,41.156442],[-8.598519,41.156433]]"

    outputFile = open(outputFilePath, "a")
    with open(inputFilePath) as infile:
        next(infile)
        reader = csv.reader(infile)
        for row in reader:
            if row[7] == "False":
                coordinatesArray = ast.literal_eval(row[8])
                if len(coordinatesArray) > 0:
                    ts = int(row[5])
                    for i in range(len(coordinatesArray)):
                        latitude, longitude = map(float, (coordinatesArray[i][1], coordinatesArray[i][0]))
                        # geoJSONStr = Feature(
                        #     geometry=Point((longitude, latitude)),
                        #     properties={
                        #         'oID': row[0],
                        #         'timestamp': datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
                        #         'taxiID': row[4]
                        #     }
                        # )
                        csvStr = row[0] + ", " + row[4] + ", " + str(ts) + ", " + str(longitude) + ", " + str(latitude)
                        # print(csvStr)
                        ts += 15

                        outputFile.write(str(csvStr))
                        outputFile.write('\n')
    outputFile.close()


def CSVToGeoJSON():

    inputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/transformedQueryTrajectories.csv"
    outputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/transformedQueryTrajectories.geojson"

    # Attributes:  TRIP_ID, TAXI_ID, TIMESTAMP, LONGITUDE, LATITUDE
    # Sample Data: 1372667893620000116, 20000116, 1372668088, -8.60805, 41.162391

    outputFile = open(outputFilePath, "a")
    with open(inputFilePath) as infile:

        reader = csv.reader(infile)
        for row in reader:
            ts = int(row[2])
            latitude, longitude = map(float, (row[4], row[3]))
            geoJSONStr = Feature(
                geometry=Point((longitude, latitude)),
                properties={
                    'oID': row[0],
                    'timestamp': datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
                    'taxiID': row[1]
                }
            )
            #print(geoJSONStr)
            outputFile.write(str(geoJSONStr))
            outputFile.write('\n')

    outputFile.close()

def extractNQueryTrajectories(n):
    inputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/data.csv"
    outputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/transformedQueryTrajectories.csv"

    # Attributes: TRIP_ID, CALL_TYPE, ORIGIN_CALL, ORIGIN_STAND, TAXI_ID, TIMESTAMP, DAYTYPE, MISSING_DATA, POLYLINE
    # "1372808091620000624","C","","","20000624","1372808091","A","False","[[-8.606448,41.14467],[-8.607033,41.144859],[-8.607717,41.143743],[-8.608158,41.143185],[-8.608185,41.142924],[-8.606016,41.142402],[-8.605179,41.143437],[-8.604585,41.144661],[-8.604378,41.145075],[-8.603838,41.145381],[-8.603496,41.145489],[-8.602137,41.145624],[-8.600427,41.145768],[-8.600418,41.146884],[-8.599221,41.147847],[-8.599059,41.147973],[-8.598681,41.148252],[-8.598672,41.148234],[-8.598663,41.148225],[-8.598762,41.149071],[-8.597682,41.151042],[-8.596377,41.15331],[-8.596332,41.153598],[-8.596458,41.153733],[-8.597205,41.15403],[-8.597934,41.154372],[-8.59896,41.154678],[-8.598762,41.155533],[-8.59851,41.155866],[-8.598366,41.156397],[-8.598411,41.156496],[-8.598582,41.156442],[-8.598519,41.156433]]"

    outputFile = open(outputFilePath, "a")
    rowsToSkip = math.floor(1710000/n)  # skipping rowsToSkip rows to extract only 100K trajectories for query
    rowSkipCounter = 0
    with open(inputFilePath) as infile:
        next(infile)
        reader = csv.reader(infile)
        for row in reader:
            if rowSkipCounter >= rowsToSkip:
                rowSkipCounter = 0
                if row[7] == "False":
                    coordinatesArray = ast.literal_eval(row[8])
                    if len(coordinatesArray) > 0:
                        ts = int(row[5])
                        for i in range(len(coordinatesArray)):
                            latitude, longitude = map(float, (coordinatesArray[i][1], coordinatesArray[i][0]))
                            csvStr = row[0] + ", " + row[4] + ", " + str(ts) + ", " + str(longitude) + ", " + str(latitude)
                            # print(csvStr)
                            ts += 15
                            outputFile.write(str(csvStr))
                            outputFile.write('\n')
            else:
                rowSkipCounter += 1
    outputFile.close()

def splitQueryTrajectoriesToGeoJSON():
    inputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/transformedQueryTrajectories.csv"
    outputFilePath = "/data1/datasets/2D_Spatial/PortugalTaxiData_PKDD15/queryTrajectories/"


    with open(inputFilePath) as infile:
        reader = csv.reader(infile)
        for row in reader:
            outputFileName = outputFilePath + row[0] + ".geojson"
            ts = int(row[2])
            latitude, longitude = map(float, (row[4], row[3]))
            geoJSONStr = Feature(
                geometry=Point((longitude, latitude)),
                properties={
                    'oID': row[0],
                    'timestamp': datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
                    'taxiID': row[1]
                }
            )
            # print(geoJSONStr)
            outputFile = open(outputFileName, "a")
            outputFile.write(str(geoJSONStr))
            outputFile.write('\n')
            outputFile.close()

