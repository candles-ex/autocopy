# auto.py
# CANDLES auto data copy script

import sys
import os
import numpy as np
from time import sleep
import datetime
import subprocess

Run = 10
MaxRunNum = 1000
sizeMatrix = np.zeros((MaxRunNum-1,MaxRunNum-1))

toDir = 'mzks@lxmzks:~/to/'
fromDir = './from/'

while True:
    copyReady = False  #check existance of next run file
    toFileList = subprocess.check_output(["ssh","mzks@lxmzks","ls","-la","to"]).decode('utf-8') #get remote file list

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
                            subprocess.call(["scp",fromfile, tofile])
                            if ssRun == 1:
                                print("copy sgl and ped", filename)
                                subprocess.call(["scp",fromDir+filenameSgl, toDir])
                                subprocess.call(["scp",fromDir+filenamePed, toDir])
                    else:
                        copyReady = True
                else:
                    sizeMatrix[sRun-1][ssRun-1] = size

    print('loop end ',datetime.datetime.now())
    sleep(10)

