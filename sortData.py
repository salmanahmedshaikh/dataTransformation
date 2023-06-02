import csv, json
import os

def main():
    # A sample tuple/record: {'geometry': {'coordinates': [116.43854, 39.88682], 'type': 'Point'}, 'properties': {'oID': '1005', 'timestamp': '2008-02-08 08:06:43'}, 'type': 'Feature'}
    # time [ms] (unixtime + milliseconds/1000), person id, position x [mm], position y [mm], position z (height) [mm], velocity [mm/s], angle of motion [rad], facing angle [rad]
    inputFilePath = "/data1/datasets/2D_Spatial/SyntheticIndividualTrajs_GaussianRW_Obj100_TI15_1M/"
    outputFilePath = "/data1/datasets/2D_Spatial/SortedSyntheticIndividualTrajs_GaussianRW_Obj100_TI15_1M/"

    for filename in os.listdir(inputFilePath):
        fileToRead = inputFilePath + filename
        fileToWrite = outputFilePath + filename

        # Opening JSON file
        f = open(fileToRead)
        # returns JSON object as
        # a dictionary

        lines = f.readlines()

        FileDict = {}

        for line in lines:
            #print(line)
            jsonData = json.loads(line)
            #print(jsonData['properties']['seqID'])
            FileDict.update({ int(jsonData['properties']['seqID']): line})

        FileDictSorted = dict(sorted(FileDict.items()))

        fileToWrite = open(fileToWrite, "a")
        for keys, values in FileDictSorted.items():
            #print(str(keys) + ", " + values)
            fileToWrite.write(values)
            # fileToWrite.write('\n')

        fileToWrite.close()


if __name__ == "__main__":
    main()
