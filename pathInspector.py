__author__ = 'STH'

import os

def getWorkingPath(metaPath):
    if isinstance(metaPath, str) and os.path.exists(metaPath):
        return os.path.dirname(metaPath)
    else:
        return False

def fileCount(metaPath):
    if os.path.exists(metaPath):
        return len([file for file in os.listdir(metaPath)])
    else:
        return False

def findNearestPathMatch(metaPath):
    pathParts = metaPath.split('\\')
    rebuildPath = ''
    for part in range(0,len(pathParts)):
        rebuildPath += pathParts[part]
        if(part<len(pathParts)-1):
            rebuildPath+="\\"
        if not(os.path.exists(rebuildPath)):
            break
    return rebuildPath

