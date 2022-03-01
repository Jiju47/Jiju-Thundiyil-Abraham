# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:18:38 2021

@author: Tailored Light
"""
from back_end_green_36 import *

def main():
#TRYING TO FIND ANY RETARDER DEVICE AND CONNECT TO IT 
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[1]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
    
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture() #Captured PM image
#**********************************************************************************Function 2 begins*********************************************************************
print("Function 2")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
        print("*** End ***")

Image_Capture1()#Captured PR image
#**********************************************************************************Function 3 begins*********************************************************************
print("Function 3")
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
        SetVoltageTo4(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture2()#Captured PP image
#**********************************************************************************Function 4 begins*********************************************************************
print("Function 4")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo6(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")

Image_Capture3()#Captured PH image
#**********************************************************************************Function 5 begins*********************************************************************
print("Function 5")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture4()#Captured PL image
#**********************************************************************************Function 6 begins*********************************************************************
print("Function 6")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture5()#Captured PV image
#**********************************************************************************Function 7 begins*********************************************************************
print("Function 7")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo15(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture6()#Captured HV image
#**********************************************************************************Function 8 begins*********************************************************************
print("Function 8")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture7()#Captured HL image
#**********************************************************************************Function 9 begins*********************************************************************
print("Function 9")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")

Image_Capture8()#Captured HR image
#**********************************************************************************Function 10 begins*********************************************************************
print("Function 10")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture9()#Captured HM image
#**********************************************************************************Function 11 begins*********************************************************************
print("Function 11")
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
        SetVoltageTo4(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture10()#Captured HP image
#**********************************************************************************Function 12 begins*********************************************************************
print("Function 12")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo6(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture11()#Captured HH image
#**********************************************************************************Function 13 begins*********************************************************************
print("Function 13")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[1]
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
        SetVoltageTo29(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture12()#Captured HP image
#**********************************************************************************Function 14 begins*********************************************************************
print("Function 14")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")

Image_Capture13()#Captured MM image
#**********************************************************************************Function 15 begins*********************************************************************
print("Function 15")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture14()#Captured LV image
#**********************************************************************************Function 16 begins*********************************************************************
print("Function 16")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture15()#Captured PV image
#**********************************************************************************Function 17 begins*********************************************************************
print("Function 17")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture16()#Captured LR image
#**********************************************************************************Function 18 begins*********************************************************************
print("Function 18")
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
        SetVoltageTo4(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture17()#Captured LP image
#**********************************************************************************Function 19 begins*********************************************************************
print("Function 19")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture18()#Captured RR image
#**********************************************************************************Function 20 begins*********************************************************************
print("Function 20")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo6(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture19()#Captured RL image
#**********************************************************************************Function 21 begins*********************************************************************
print("Function 21")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture20()#Captured RV image
#**********************************************************************************Function 22 begins*********************************************************************
print("Function 22")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture21()#Captured RM image
#**********************************************************************************Function 23 begins*********************************************************************
print("Function 23")
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
        SetVoltageTo4(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture22()#Captured RP image
#**********************************************************************************Function 24 begins*********************************************************************
print("Function 24")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo6(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture23()#Captured RH image
#**********************************************************************************Function 25 begins*********************************************************************
print("Function 25")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[1]
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
        SetVoltageTo18(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture24()#Captured MH image
#**********************************************************************************Function 26 begins*********************************************************************
print("Function 26")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture25()#Captured ML image
#**********************************************************************************Function 27 begins*********************************************************************
print("Function 27")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture26()#Captured PV image
#**********************************************************************************Function 28 begins*********************************************************************
print("Function 28")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo15(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture27()#Captured VV image
#**********************************************************************************Function 29 begins*********************************************************************
print("Function 29")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture28()#Captured VL image
#**********************************************************************************Function 30 begins*********************************************************************
print("Function 30")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture29()#Captured VR image
#**********************************************************************************Function 31 begins*********************************************************************
print("Function 31")
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture30()#Captured VM image
#**********************************************************************************Function 32 begins*********************************************************************
print("Function 32")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture31()#Captured MM image
#**********************************************************************************Function 33 begins*********************************************************************
print("Function 33")
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
        SetVoltageTo5(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture32()#Captured MR image
#**********************************************************************************Function 34 begins*********************************************************************
print("Function 34")
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
        SetVoltageTo4(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture33()#Captured MP image
#**********************************************************************************Function 35 begins*********************************************************************
print("Function 35")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[3]
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
        SetVoltageTo15(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture34()#Captured VP image
#**********************************************************************************Function 36 begins*********************************************************************
print("Function 36")
try:
        devs = LCC25ListDevices()
        print(devs)
        if(len(devs)<=0):
           print('There is no devices connected')
           exit()
        LCC25 = devs[2]
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
        SetVoltageTo6(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture35()#Captured VH image

print ("36 Images captured for Green Laser with 532nm")
main()