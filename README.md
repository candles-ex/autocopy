
# CANDLES Data transportation tool
Author  : K. Mizukoshi
Date    : 2018 Aug. 28

## Overview
This script is to transport CANDLES raw data on time.
The auto.py watch a data directory, transport the data that satisfies the following conditions.

- No update in 10 minutes.
- The next run has been started.
- The file has not been created in the directory transported.

## Usage
```
>nohup python auto.py &
```
Then, a shifter doesn't have to do an additional work.

## Monitoring / troubleshoot
```
>ps ux | grep auto

candles 17112   0.0  0.2  4385384  15264 s007  SN    8:05PM   0:00.87 python auto.py
```
If you cannot find the process, see nohup.out.

You can

#. restart this script
#. transport the data using autocopy.sh 
#. report me (K. Mizukoshi mzks@ne.phys.sci.osaka-u.ac.jp) and exparts.

