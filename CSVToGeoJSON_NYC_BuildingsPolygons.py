import csv, json
import os
from decimal import Decimal
from geojson import Feature, FeatureCollection, Point, Polygon
import geopandas as gpd
import geojson

def main():


    outputFilePath = "/data1/datasets/NYC_Data/ConvenienceStore_Related/NYC_Building/geoJSON/geoJSONFeatures.geojson"
    geoJSONFilePath = "/data1/datasets/NYC_Data/ConvenienceStore_Related/NYC_Building/BuildingFootprints.geojson"

    # Attributes: BIN, the_geom, NAME, CNSTRCT_YR, LSTMODDATE, LSTSTATYPE, DOITT_ID, HEIGHTROOF, FEAT_CODE, GROUNDELEV, SHAPE_AREA, SHAPE_LEN, BASE_BBL, MPLUTO_BBL, GEOMSOURCE
    # 3394646,"MULTIPOLYGON (((-73.87129515296562 40.65717370043455, -73.87135858020156 40.65714663518705, -73.87143322008981 40.6572480836196, -73.87136979278591 40.6572751498085, -73.87129515296562 40.65717370043455)))",,2009,08/22/2017 12:00:00 AM +0000,Constructed,1212853,21.60850812,2100,18,854.66243317866,125.0797955584,3044520815,3044520815,Photogramm

    with open(geoJSONFilePath) as f:
        gj = geojson.load(f)
    #features = gj['features'][0]

    features = gj['features']
    fileToWrite = open(outputFilePath, "a")
    
    # for x in features:
    #     fileToWrite.write(str(x))
    #     fileToWrite.write('\n') 
    # fileToWrite.close()
    
    for x in features:
        print(x.)



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