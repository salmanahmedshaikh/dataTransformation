import csv, json
import os
from decimal import Decimal
from geojson import Feature, FeatureCollection, Point



def main():
    # A sample tuple/record: 1351039728.980,9471001,-22366,2452,1261.421,780.711,-2.415,-2.441
    # time [ms] (unixtime + milliseconds/1000), person id, position x [mm], position y [mm], position z (height) [mm], velocity [mm/s], angle of motion [rad], facing angle [rad]
    csvFilePath = "/data1/datasets/2D_Spatial/ATC_ShoppingMall/CSV/"
    jsonFilePath = "/data1/datasets/2D_Spatial/ATC_ShoppingMall/GeoJSON/"

    for filename in os.listdir(csvFilePath):
        fileToRead = csvFilePath + filename
        #fileToWrite = jsonFilePath + filename

        #fileToWrite = open(fileToWrite, "a")
        minX = 9999999.99999
        maxX = -9999999.99999
        minY = 9999999.99999
        maxY = -9999999.99999
        with open(fileToRead, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for timestamp, oID, x, y, z, vel, angle, fAngle in reader:

                x_ = float(x)
                y_ = float(y)

                if x_ < minX:
                    minX = x_

                if y_ < minY:
                    minY = y_

                if x_ > maxX:
                    maxX = x_

                if y_ > maxY:
                    maxY = y_

                #timestamp_ms = float(timestamp) * 1000

                #ｘ, y, z = map(float, (x, y, z))
                #str1 = Feature(
                #    geometry=Point((x, y, z)),
                #    properties={
                #        'oID': oID,
                #        'timestamp': int(timestamp_ms)
                #    }
                #)

                #fileToWrite.write(str(str1))
                #fileToWrite.write('\n')

        #fileToWrite.close()
        print("minX " + str(minX))
        print("maxX " + str(maxX))
        print("minY " + str(minY))
        print("maxY " + str(maxY))


if __name__== "__main__":
  main()