# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:18:38 2021

@author: Tailored Light
"""
from back_end_green_16 import *

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
        SetVoltageTo8(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
        print("*** End ***")

Image_Capture1()#Captured PP image
#**********************************************************************************Function 3 begins*********************************************************************
print("Function 3")
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
        SetVoltageTo9(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture2()#Captured PH image
#**********************************************************************************Function 4 begins*********************************************************************
print("Function 4")
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
        SetVoltageTo85(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")

Image_Capture3()#Captured HH image
#**********************************************************************************Function 5 begins*********************************************************************
print("Function 5")
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
        SetVoltageTo2(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture4()#Captured VH image
#**********************************************************************************Function 6 begins*********************************************************************
print("Function 6")
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
Image_Capture5()#Captured MH image
#**********************************************************************************Function 7 begins*********************************************************************
print("Function 7")
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
Image_Capture6()#Captured MP image
#**********************************************************************************Function 8 begins*********************************************************************
print("Function 8")
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
        SetVoltageTo85(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture7()#Captured VP image
#**********************************************************************************Function 9 begins*********************************************************************
print("Function 9")
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

Image_Capture8()#Captured VM image
#**********************************************************************************Function 10 begins*********************************************************************
print("Function 10")
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
        SetVoltageTo9(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture9()#Captured VV image
#**********************************************************************************Function 11 begins*********************************************************************
print("Function 11")
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
Image_Capture10()#Captured HV image
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
        SetVoltageTo25(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture11()#Captured VM image
#**********************************************************************************Function 13 begins*********************************************************************
print("Function 13")
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
        SetVoltageTo8(hdl)                              
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
        SetVoltageTo2(hdl)                              
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
        SetVoltageTo9(hdl)                              
#ERROR: THIS USUALLY COMES INTO PLAY WHEN ONE DIDNT DISCONNECT THE RETARDER AFTER SETTING A VOLTAGE        
except Exception as ex:
        print("Warning:", ex)
print("*** End ***")
Image_Capture14()#Captured MV image
#**********************************************************************************Function 16 begins*********************************************************************
print("Function 16")
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
Image_Capture15()#Captured PV image
print ("16 Images captured for Blue Laser with 445nm")
main()
