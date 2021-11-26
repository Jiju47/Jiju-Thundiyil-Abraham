# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 07:46:30 2021
IMPORTANT:
    - the .dll file ("LCC25CommandLib_win32") must be in the same directory
    - the sdk/library from thorlabs for the retarders only works with a 32-bit Python (NOT 64-bit!)
    
ABOUT THE functions:
    - LCR_calibration_function_1.py: This is just for running once in the beginning to see wether the connection is working properly. It sets the voltage at the connected retarder to zero
    -LCR_calibration_function_2.py: This starts from zero volts and goes up in tiny steps to 25 volts. Other functions to get camera measurements have to be implemented here.
@author: Lennart
"""

from LCC25_COMMAND_LIB import *
import time

def IncreaseVoltageByDeltaV(hdl,DeltaV):
    #Setting the output mode to voltage1    
    result=LCC25SetOutputMode(hdl, 1) # 0:modulation,1:voltage1,2:voltage2
    if(result<0):
       print("set OutputMode failed", result)
    else:
       print("set OutputMode to voltage1 ")
    outputmode=[0] 
    outputmodeList={0:"modulation",1:"voltage1",2:"voltage2"}
    result=LCC2GetOutputMode(hdl, outputmode)
    if(result<0):
       print("get OutputMode failed", result)
    else:
       print("get OutputMode: ", outputmodeList.get(outputmode[0]))
    
    #Getting the current voltage of the retarder with the handle hdl 
    Vol1=[0] 
    result=LCC25GetVoltage1(hdl, Vol1)
    if(result<0):
       print("get Voltage1 failed", result)
    else:
       print("get Voltage1: ", Vol1)
    
    #Increasing the current voltage by a tiny step DeltaV. The step size can be spezified in the main function   
    Vol1=(Vol1[0])  
    Vol1=Vol1+DeltaV   
    #Setting the voltage of the retarder with handle hdl to the new voltage
    result=LCC25SetVoltage1(hdl, Vol1)
    if(result<0):
       print("set Voltage1 failed", result)
    else:
       print("set Voltage1 to Vol1 ")
    #Stopping the connection with the current connected retarder to avoid complications elsewhere   
    LCC25Close(hdl) 
    #Printing and returning the new voltage
    CurrentVoltage=Vol1
    print(CurrentVoltage)
    return CurrentVoltage

def main():
    CurrentVoltage=0
    while CurrentVoltage < 24.999:
        #Checking device connection and connecting to device
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
            print('There is no devices connected')
            exit()
        LCC25 = devs[0]
        sn = LCC25[0]
        print("connect ", sn)
        hdl = LCC25Open(sn, 115200, 3)
        if(hdl<0):
                print("open ", sn, " failed")
                exit()
        if(LCC25IsOpen(sn) == 0):
                print("LCC25IsOpen failed")
                LCC25Close(hdl)
                exit() 
        #increasing the current voltage by a step(0.001 Volts is the tiniest step possible)                    
        CurrentVoltage=IncreaseVoltageByDeltaV(hdl,0.001)
        #INSERT CAMERA-MEASUREMENT-FUNCTION HERE                
               
    print("*** Final End ***")
        



    
