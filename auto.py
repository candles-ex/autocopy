# auto.py
# CANDLES auto data copy script
# using python2 for DAQ module

import sys
import os
from time import sleep
import datetime
import commands

# Directory setting
Run = 10
hostName = 'candles@kmcands'
toDir = hostName + ':/Data5/candles/DATA/DaqmwData20130527/'
fromDir = '/data/can3data20130510/'
dataDisk = 'Data5'


MaxRunNum = 1000
sizeMatrix = [[ 0. for column in range(MaxRunNum-1)] for row in range(MaxRunNum-1)]

while True:

    # check capacity
    commandSize = 'ssh ' + hostName + ' df --block-size=1G | grep ' + dataDisk + '| tr -s " " | cut -d" " -f 4'
    availableSize = int(commands.getoutput(commandSize))
    if availableSize < 100:
        print('No enough capacity in transported disk')
        sys.exit()

    copyReady = False  #check existance of next run file
    command1 = "ssh " + hostName + " ls -la to"
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
                    if copyReady == True:
                        if toFileList.find(filename) == -1:
                            print("copy", filename)
                            commands.getoutput("scp "+ fromfile + " " + tofile)
                            if ssRun == 1:
                                print("copy sgl and ped", filename)
                                commands.getoutput("scp "+fromDir+filenameSgl+ " " + toDir)
                                commands.getoutput("scp "+fromDir+filenamePed+ " " + toDir)
                    else:
                        copyReady = True
                else:
                    sizeMatrix[sRun-1][ssRun-1] = size

    print('loop end ',datetime.datetime.now())
    sleep(600) 

