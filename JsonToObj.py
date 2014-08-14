__author__ = 'STH'

import os
import json
import re

class JsonToObj:
    jsonPath = ''
    jsonData = {}
    def __init__(self,path=False):
        if(path and os.path.exists(path)):
            self.jsonPath = path

    def hasPath(self):
        return self.jsonPath and len(self.jsonPath) > 0 and os.path.exists(self.jsonPath)

    def validateJson(self):
        if self.hasPath():
            return True
        else:
            return False

    def repairJson(self):
        if self.hasPath():
            return True
        else:
            return False

    def loadJson(self):
        if self.validateJson():
            try:
                json_file = open(self.jsonPath)
                json_load = json.load(json_file)
                json_file.close()
                if(json_load):
                    self.jsonData = json_load
                    return True
                else:
                    return False
            except ValueError:
                return False
        else:
            return False

    def makeMetaJsonFile(self):
        if self.hasPath():
            print(os.getcwd())
            os.chdir(self.jsonPath)
            print(os.getcwd())
            if not os.path.exists("metanote.json"):
                open("metanote.json","a").close()
                return True
            else:
                return False
        else:
            return False














