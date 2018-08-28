# auto.py
# CANDLES auto data copy script

import sys
import os
import glob
import numpy as np
from time import sleep
import shutil
import subprocess

Run = 10
MaxRunNum = 10 #1000

sizeMatrix = np.zeros((MaxRunNum-1,MaxRunNum-1))

while True:
    copyReady = False  #check existance of next run file
    toFileList = subprocess.check_output(["ssh","mzks@lxmzks","ls","-la","to"]).decode('utf-8')   
    for sRun in reversed(range(1,MaxRunNum)):
        for ssRun in reversed(range(1,MaxRunNum)):
            filename = 'Run' + str(Run).zfill(3) + '-' + str(sRun).zfill(3) + '-' + str(ssRun).zfill(3) + '.dat'
            fromfile = './from/' + filename
            tofile = 'mzks@lxmzks:~/to/' + filename

            if os.path.exists(fromfile) == True:
                size = os.path.getsize(fromfile)
                if sizeMatrix[sRun-1][ssRun-1] == size:
                    if copyReady == True:
                        if toFileList.find(filename) == -1:
                            print("copy", filename)
                            #shutil.copy2(fromfile, tofile)
                            subprocess.call(["scp",fromfile, tofile])
                    else:
                        copyReady = True
                else:
                    sizeMatrix[sRun-1][ssRun-1] = size

    sleep(10)

