import pandas
import numpy
import datetime
import time


TimeToRun = #in seconds
#Resulting bins
TimeResult = []
EnergyResult = [[0,0], [20,0], [40,0], [60,0], [80,0] [100,0]]
DirectionResult = []

time_Delta = #time in between intervals for TimeResult bins
timeCount = 0 #count for time bins
binstart = time.time() #time.time() is current time

t_end = time.time() + TimeToRun


while time.time() < t_end:

    #import textfile? with timestamp, count, and energy per particle of a frame
    frame_TimeStamp = 
    frame_Count = 
    frame_EnergyPerParticle = {}
    frame_Direction = {x,y,z} #magnetometer needed to determine
    
    if frameTimeStamp < binstart+time_Delta:
        timeCount = += 1

    if frameTimeStamp >= binstart+time_Delta:
        TimeResult.append([binstart, timeCount])
        binstart = time.time() #once appended new bin is created for next time slot
        timeCount = 0 #reset count to 0

    for particleEnergy in frameEnergyperParticle:
        if particleEnergy < 20 :
            EnergyResult[0][1] += 1
        if 20 <= particleEnergy < 40:
            EnergyResult[1][1] += 1
        if 40 <= particleEnergy < 60:
            EnergyResult[2][1] += 1
        if 60 <= particleEnergy < 80:
            EnergyResult[3][1] += 1
        if 80 <= particleEnergy < 100:
            EnergyResult[4][1] += 1
        if particleEnergy >= 100 :
            EnergyResult[5][1] += 1

    
            
