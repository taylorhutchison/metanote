__author__ = 'STH'

import argparse
import io


def setArgs():
    argumentParser = argparse.ArgumentParser(description="Process Metanote path and options.")
    argumentParser.add_argument('--path', type=str, required=False, help="Set a path different from current directory.")
    argumentParser.add_argument('--overwrite', action='store_true', required=False, help="Overwrite any existing metanote file.")
    argumentParser.add_argument('--edit', action='store_true', required=False, help="Enter editor mode after generating new metanote file.")
    argumentParser.add_argument('--repair', action='store_true', required=False, help="Attempt to repair metanote file if it has been altered.")

    return argumentParser.parse_args()

def processCommand(i):
    return True

def enterLoop(args=False):
    if(args):
        i = ''
        while(i!='exit'):
            i = input("Enter command: ")
            processCommand(i)
    else:
        return False

