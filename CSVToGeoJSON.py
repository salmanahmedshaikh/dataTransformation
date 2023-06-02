import csv, json
import os
from geojson import Feature, FeatureCollection, Point

csvFilePath = "/media/salman/DATA/Datasets/2D_Spatial/NYC_Data/FourSquareCheckIns/dataset_TSMC2014_NYC.csv"
jsonFilePath = "/media/salman/DATA/Datasets/2D_Spatial/NYC_Data/FourSquareCheckIns/dataset_TSMC2014_NYC.json"


#features = []
fToWriteTmp = open(jsonFilePath, "a")
with open(csvFilePath, newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for oID, venueID, venueCatID, venueName, latitude, longitude, timeZoneOffset, day, month, date, timestamp, timestamp2, code, year in reader:
        latitude, longitude = map(float, (latitude, longitude))
        str = Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'oID': oID,
                    'timestamp': timestamp,
		            'venueName': venueName
                }
            )
        fToWriteTmp.write(str(str1))
        fToWriteTmp.write('\n')
#        features.append(str)
fToWriteTmp.close()

#collection = FeatureCollection(features)
#with open(jsonFilePath, "w") as f:
#    f.write('%s' % collection)

