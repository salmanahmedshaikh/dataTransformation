import csv, json
import os
from decimal import Decimal
from geojson import Feature, FeatureCollection, Point



def main():
    # Sample data: {"geometry": {"coordinates": [116.40181, 39.95289], "type": "Point"}, "properties": {"oID": "1600", "timestamp": "2008-02-08 14:13:28"}, "type": "Feature"}
    csvFilePath = "/media/salman/DATA/Datasets/2D_Spatial/T-driveTaxiTrajectories/taxi_log_2008_by_id/"
    jsonFilePath = "/media/salman/DATA/Datasets/2D_Spatial/T-driveTaxiTrajectories/taxi_log_2008_by_id_GeoJSON/"

    for filename in os.listdir(csvFilePath):
        fileToRead = csvFilePath + filename
        fileToWrite = jsonFilePath + filename

        fileToWrite = open(fileToWrite, "a")
        with open(fileToRead, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for oID, timestamp, longitude, latitude in reader:

                if validCoordinates(longitude, latitude):
                    latitude, longitude = map(float, (latitude, longitude))
                    str1 = Feature(
                        geometry=Point((longitude, latitude)),
                        properties={
                            'oID': oID,
                            'timestamp': timestamp
                        }
                    )

                    fileToWrite.write(str(str1))
                    fileToWrite.write('\n')

        fileToWrite.close()

# The latitude must be a number between -90 and 90 and the longitude between -180 and 180
def validCoordinates(longitude_, latitude_):

    long = Decimal(longitude_)
    lat = Decimal(latitude_)

    #print(long.as_tuple().exponent)
    #print(lat.as_tuple().exponent)

    # Boundary for Beijing
    if (115.5 < Decimal(longitude_) < 117.6) and (39.6 < Decimal(latitude_) < 41.1) and abs(long.as_tuple().exponent) > 3 and abs(lat.as_tuple().exponent) > 3:
        return True
    else:
        return False


if __name__== "__main__":
  main()