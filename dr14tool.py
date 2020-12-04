#!/usr/bin/python

import os
from fnmatch import fnmatch

def sanitizeFileName(fileName):
    # Check if the last character is a trailing / or \
    if (fileName[-1:] in ['/', '\\']):
        fileName = fileName[:-1]  # Strip the last character
    return fileName

# Body 
import argparse
parser = argparse.ArgumentParser(description='Tooling for dr14_tmeter.')

parser.add_argument('sourcefolder', metavar='sourcefolder', type=str, help='root-folder containing music files (flac)')
parser.add_argument('-s', '--scan', help="scan for missing dr14.txt files and generate when needed (default)", action="store_true")
parser.add_argument('-r', '--report', help="report for all dr14.txt files", action="store_true")   

args = parser.parse_args()

source_tree = sanitizeFileName(args.sourcefolder)
scanMode = args.scan
reportMode = args.report

if not scanMode and not reportMode:
    scanMode = True
if scanMode and reportMode:
    reportMode = False

for dir, dirNames, fileNames in os.walk(source_tree):
    dirNames.sort()

    if scanMode:
        print(dir)
        for fileName in sorted(fileNames):
            fullFileName = os.path.join(dir, fileName)
            if fnmatch(fullFileName, "*.flac"):   
                dr14FileFound = False         
                for fileName in sorted(fileNames):
                    fullFileName = os.path.join(dir, fileName)
                    if fnmatch(fullFileName, "*/dr14.txt"):
                        dr14FileFound = True
                        break
                if not dr14FileFound:
                    os.system('dr14_tmeter "' + dir + '"')
                break

    if reportMode:
        for fileName in sorted(fileNames):
            fullFileName = os.path.join(dir, fileName)
            if fnmatch(fullFileName, "*/dr14.txt"):
                valueAsAstring = os.popen('cat "' + dir + '/dr14.txt" | grep "Official DR value:" | cut -c24-27 &> /dev/null').read().strip()
                if len(valueAsAstring) < 2:
                    valueAsAstring = '0' + valueAsAstring
                dirName = dir.replace(source_tree + '/', '')
                print(valueAsAstring + ' ' + dirName)
                break        

