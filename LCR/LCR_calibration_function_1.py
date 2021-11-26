# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 07:35:10 2021
IMPORTANT:
    - the .dll file ("LCC25CommandLib_win32") must be in the same directory
    - the sdk/library from thorlabs for the retarders only works with a 32-bit Python (NOT 64-bit!)
@author: Lennart
"""
#IMPORTS
from LCC25_COMMAND_LIB import *
import time

#FUNCTIONS
def SetVoltageToZero(hdl):
#THE OUTPUT MODE FOR THE VOLTAGE HAS TO BE SET   
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

#SETTING A VOLTAGE ON THE RETARDER WITH HANDLE HDL, NUMBER IS THE VOLTAGE THAT WILL BE SET    
    result=LCC25SetVoltage1(hdl, 0) 
    if(result<0):
       print("set Voltage1 failed", result)
    else:
       print("set Voltage1 to 0 ")
#RETARDER NEEDS TO BE DISCONNECTED, OTHERWISE IT WILL TRHOW AN ERROR IF ONE TRIES TO CONNECT TO IT TWICE IN THE SAME RUN
    LCC25Close(hdl)   
      
def main():
#TRYING TO FIND ANY RETARDER DEVICE AND CONNECT TO IT (ONLY WORKS WITH ONE RETARDER AT THIS POINT)
    print("*** Testing Connection to Device  ***")
    try:
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
#A SELFWRITTEN FUNCTION THAT SETS THE VOLTAGE OF THE RETARDER WITH THE HANDLE HDL TO ZERO 
        SetVoltageToZero(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
    
#RUNNING MAIN FUNCTION    
main()