__author__ = 'STH'

import os
import clitools
import pathInspector
from JsonToObj import JsonToObj



if __name__ == '__main__':
    args = clitools.setArgs()
    if args.path == None:
        workingFolder = os.getcwd()
    else:
        workingFolder = pathInspector.getWorkingPath(args.path)

    if workingFolder:
        metanotePath = workingFolder + "\metanote.json"

        if os.path.exists(metanotePath):
            metanote = JsonToObj(metanotePath)
        else:
            metanote = JsonToObj(workingFolder)
            metanote.makeMetaJsonFile()

        if not metanote.validateJson():
            if args.repair:
                metanote.repairJson()
            else:
                print("Metafile validation error. Attempt to repair by adding --repair flag.")
        else:
            metanote.loadJson()

        print(metanote.jsonData)

    else:
        print(pathInspector.findNearestPathMatch(args.path))







