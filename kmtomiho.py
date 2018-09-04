#   ____    _    _   _ ____  _     _____ ____  
#  / ___|  / \  | \ | |  _ \| |   | ____/ ___| 
# | |     / _ \ |  \| | | | | |   |  _| \___ \ 
# | |___ / ___ \| |\  | |_| | |___| |___ ___) |
#  \____/_/   \_\_| \_|____/|_____|_____|____/ 
#                                              
# kmtomiho.py
# CANDLES auto data copy script
# using python2 for kmcands


import sys
import os
from time import sleep
import datetime
import commands

# Directory setting
Run = 10
hostName = 'miho'
dirName = '/np1c/v01/candles/CANUG/RawData/DaqmwData2013.05.27/'
toDir = hostName + ':' + dirName
fromDir = '/Data5/candles/DATA/DaqmwData20130527/'


MaxRunNum = 1000
sizeMatrix = [[ 0. for column in range(MaxRunNum-1)] for row in range(MaxRunNum-1)]

while True:

    command1 = "ssh " + hostName + " ls -la " + dirName
    toFileList = commands.getoutput(command1)

    for sRun in reversed(range(1,MaxRunNum)):
        for ssRun in reversed(range(1,MaxRunNum)):
            filename = 'Run' + str(Run).zfill(3) + '-' + str(sRun).zfill(3) + '-' + str(ssRun).zfill(3) + '.dat'
            fromfile = fromDir + filename
            tofile = toDir + filename

            filenameSgl = 'Sgl' + str(Run).zfill(3) + '-' + str(sRun).zfill(3) + '-001.dat'
            filenamePed = 'Ped' + str(Run).zfill(3) + '-' + str(sRun).zfill(3) + '-001.dat'

            if os.path.exists(fromfile) == True:
                size = os.path.getsize(fromfile)
                if sizeMatrix[sRun-1][ssRun-1] == size:
                    if toFileList.find(filename) == -1:
                        print("copy", filename)
                        commands.getoutput("scp "+ fromfile + " " + tofile)
                        if ssRun == 1:
                            print("copy sgl and ped", filename)
                            commands.getoutput("scp "+fromDir+filenameSgl+ " " + toDir)
                            commands.getoutput("scp "+fromDir+filenamePed+ " " + toDir)
                else:
                    sizeMatrix[sRun-1][ssRun-1] = size

    print('loop end ',datetime.datetime.now())
    sleep(10) 

