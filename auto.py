# auto.py
# CANDLES auto data copy script

import sys
import os
import glob
import numpy as np
from time import sleep
import shutil


Run = 10
MaxRunNum = 10 #1000

sizeMatrix = np.zeros((MaxRunNum-1,MaxRunNum-1))

while True:
    copyReady = False  #check existance of next run file
    
    for sRun in reversed(range(1,MaxRunNum)):
        for ssRun in reversed(range(1,MaxRunNum)):
            filename = 'Run' + str(Run).zfill(3) + '-' + str(sRun).zfill(3) + '-' + str(ssRun).zfill(3) + '.dat'
            fromfile = './from/' + filename
            tofile = './to/' + filename

            if os.path.exists(fromfile) == True:
                size = os.path.getsize(fromfile)
                if sizeMatrix[sRun-1][ssRun-1] == size:
                    if copyReady == True:
                        if os.path.exists(tofile) == False:
                            print("copy", filename)
                            shutil.copy2(fromfile, tofile)
                    else:
                        copyReady = True
                else:
                    sizeMatrix[sRun-1][ssRun-1] = size

    sleep(600)

