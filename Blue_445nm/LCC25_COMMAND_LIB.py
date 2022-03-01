

from ctypes import *

#region import dll functions

LCC25Lib = cdll.LoadLibrary("LCC25CommandLib_win32.dll")

cmdList = LCC25Lib.List
cmdList.restype=c_int
cmdList.argtypes=[c_char_p, c_int]

cmdOpen = LCC25Lib.Open
cmdOpen.restype=c_int
cmdOpen.argtypes=[c_char_p, c_int, c_int]

cmdIsOpen = LCC25Lib.IsOpen
cmdIsOpen.restype=c_int
cmdIsOpen.argtypes=[c_char_p]

cmdGetVoltage1 = LCC25Lib.GetVoltage1
cmdGetVoltage1.restype=c_int
cmdGetVoltage1.argtypes=[c_int, POINTER(c_double)]

cmdGetVoltage2 = LCC25Lib.GetVoltage2
cmdGetVoltage2.restype=c_int
cmdGetVoltage2.argtypes=[c_int, POINTER(c_double)]

cmdGetModulationFrequency = LCC25Lib.GetModulationFrequency
cmdGetModulationFrequency.restype=c_int
cmdGetModulationFrequency.argtypes=[c_int, POINTER(c_double)]

cmdGetOutputMode = LCC25Lib.GetOutputMode
cmdGetOutputMode.restype=c_int
cmdGetOutputMode.argtypes=[c_int, POINTER(c_int)]

cmdGetOutputEnable = LCC25Lib.GetOutputEnable
cmdGetOutputEnable.restype=c_int
cmdGetOutputEnable.argtypes=[c_int, POINTER(c_int)]

cmdGetExternalModulation = LCC25Lib.GetExternalModulation
cmdGetExternalModulation.restype=c_int
cmdGetExternalModulation.argtypes=[c_int, POINTER(c_int)]

cmdGetPreset = LCC25Lib.GetPreset
cmdGetPreset.restype=c_int
cmdGetPreset.argtypes=[c_int, c_int]

cmdGetTestModeDwellTimeMS = LCC25Lib.GetTestModeDwellTimeMS
cmdGetTestModeDwellTimeMS.restype=c_int
cmdGetTestModeDwellTimeMS.argtypes=[c_int, POINTER(c_int)]

cmdGetTestModeIncrement = LCC25Lib.GetTestModeIncrement
cmdGetTestModeIncrement.restype=c_int
cmdGetTestModeIncrement.argtypes=[c_int, POINTER(c_double)]

cmdGetTestMinVoltage = LCC25Lib.GetTestMinVoltage
cmdGetTestMinVoltage.restype=c_int
cmdGetTestMinVoltage.argtypes=[c_int, POINTER(c_double)]
   
cmdGetTestMaxVoltage = LCC25Lib.GetTestMaxVoltage
cmdGetTestMaxVoltage.restype=c_int
cmdGetTestMaxVoltage.argtypes=[c_int, POINTER(c_double)]

cmdGetTestMinVoltage = LCC25Lib.GetTestMinVoltage
cmdGetTestMinVoltage.restype=c_int
cmdGetTestMinVoltage.argtypes=[c_int, POINTER(c_double)]
   
cmdRunTestMode = LCC25Lib.RunTestMode
cmdRunTestMode.restype=c_int
cmdRunTestMode.argtypes=[c_int]

cmdGetId = LCC25Lib.GetId
cmdGetId.restype=c_int
cmdGetId.argtypes=[c_int, c_char_p]

cmdRestoreDefaultParameters = LCC25Lib.RestoreDefaultParameters
cmdRestoreDefaultParameters.restype=c_int
cmdRestoreDefaultParameters.argtypes=[c_int]

cmdSaveParameters = LCC25Lib.SaveParameters
cmdSaveParameters.restype=c_int
cmdSaveParameters.argtypes=[c_int]

cmdSetVoltage1 = LCC25Lib.SetVoltage1
cmdSetVoltage1.restype=c_int
cmdSetVoltage1.argtypes=[c_int, c_double]

cmdSetVoltage2 = LCC25Lib.SetVoltage2
cmdSetVoltage2.restype=c_int
cmdSetVoltage2.argtypes=[c_int, c_double]

cmdSetModulationFrequency = LCC25Lib.SetModulationFrequency
cmdSetModulationFrequency.restype=c_int
cmdSetModulationFrequency.argtypes=[c_int, c_double]

cmdSetOutputMode = LCC25Lib.SetOutputMode
cmdSetOutputMode.restype=c_int
cmdSetOutputMode.argtypes=[c_int, c_int]

cmdSetOutputEnable = LCC25Lib.SetOutputEnable
cmdSetOutputEnable.restype=c_int
cmdSetOutputEnable.argtypes=[c_int, c_int]

cmdSetExternalModulation = LCC25Lib.SetExternalModulation
cmdSetExternalModulation.restype=c_int
cmdSetExternalModulation.argtypes=[c_int, c_int]

cmdSetPreset = LCC25Lib.SetPreset
cmdSetPreset.restype=c_int
cmdSetPreset.argtypes=[c_int, c_int]

cmdSetTestModeDwellTimeMS = LCC25Lib.SetTestModeDwellTimeMS
cmdSetTestModeDwellTimeMS.restype=c_int
cmdSetTestModeDwellTimeMS.argtypes=[c_int, c_int]

cmdSetTestModeIncrement = LCC25Lib.SetTestModeIncrement
cmdSetTestModeIncrement.restype=c_int
cmdSetTestModeIncrement.argtypes=[c_int, c_double]

cmdSetTestMinVoltage = LCC25Lib.SetTestMinVoltage
cmdSetTestMinVoltage.restype=c_int
cmdSetTestMinVoltage.argtypes=[c_int, c_double]

cmdSetTestMaxVoltage = LCC25Lib.SetTestMaxVoltage
cmdSetTestMaxVoltage.restype=c_int
cmdSetTestMaxVoltage.argtypes=[c_int, c_double]

cmdSetRemote = LCC25Lib.SetRemote
cmdSetRemote.restype=c_int
cmdSetRemote.argtypes=[c_int, c_int]

#endregion

def LCC25ListDevices():
    """ List all connected LCC25 devices
    Returns: 
       The LCC25 device list, each deice item is serialNumber/COM
    """
    str = create_string_buffer(1024, '\0')
    result = cmdList(str,1024)
    devicesStr = str.raw.decode("utf-8","ignore").rstrip('\x00').split(',')
    length = len(devicesStr)
    i=0
    devices=[]
    devInfo=["",""]
    while(i<length):
        str = devicesStr[i]
        if (i%2 == 0):
            if str != '':
                devInfo[0] = str
            else:
                i+=1
        else:
            devInfo[1] = str
            devices.append(devInfo.copy())
        i+=1
    return devices

def LCC25Open(serialNo, nBaud, timeout):
    """ Open device
    Args:
        serialNo: serial number of LCC25 device
        nBaud: bit per second of port
        timeout: set timeout value in (s)
    Returns: 
        non-negative number: hdl number returned Successful; negative number: failed.
    """
    return cmdOpen(serialNo.encode('utf-8'), nBaud, timeout)

def LCC25IsOpen(serialNo):
    """ Check opened status of device
    Args:
        serialNo: serial number of device
    Returns: 
        0: device is not opened; 1: device is opened.
    """
    return cmdIsOpen(serialNo.encode('utf-8'))

def LCC25Close(hdl):
    """ Close opened device
    Args:
        hdl: the handle of opened device
    Returns: 
        0: Success; negative number: failed.
    """
    return LCC25Lib.Close(hdl)

def LCC25GetId(hdl, ID):
    """get the LCC25 id
    Args:
        hdl: the handle of opened device
        ID: output string (<255)
    Returns: 
        0: Success; negative number: failed.
    """
    deviceid = create_string_buffer(1024, '\0')
    ret = cmdGetId(hdl, deviceid)
    ID[0] = deviceid.raw.decode("utf-8","ignore").rstrip('\x00').replace(">\r\n", "")
    return ret

def LCC25GetVoltage1(hdl, vol1):
    """  Return the current voltage set for Voltage 1
    Args:
        hdl: the handle of opened device
        vol: LCC25 voltage1 value
    Returns: 
        0: Success; negative number: failed.
    """
    Voltage1 = c_double(0)
    ret = cmdGetVoltage1(hdl, Voltage1)
    vol1[0] = Voltage1.value
    return ret

def LCC25GetVoltage2(hdl, vol2):
    """  Return the current voltage set for Voltage 2
    Args:
        hdl: the handle of opened device
        vol2: LCC25 voltage2 value
    Returns: 
        0: Success; negative number: failed.
    """
    Voltage2 = c_double(0)
    ret = cmdGetVoltage2(hdl, Voltage2)
    vol2[0] = Voltage2.value
    return ret

def LCC25GetModulationFrequency(hdl, freq):
    """  Return the current modulation frequency
    Args:
        hdl: the handle of opened device
        freq: LCC25 modulation frequency 
    Returns:
        0: Success; negative number: failed.
    """
    frequency = c_double(0)
    ret = cmdGetModulationFrequency(hdl, frequency)
    freq[0] = frequency.value
    return ret

def LCC2GetOutputMode(hdl, outputmode):
    """  Return the current output mode
    Args:
        hdl: the handle of opened device
        outputmode: LCC25 output mode. 0:modulation,1:voltage1,2:voltage2 
    Returns:
        0: Success; negative number: failed.
    """
    OPmode = c_int(0)
    ret = cmdGetOutputMode(hdl, OPmode)
    outputmode[0] = OPmode.value
    return ret

def LCC25GetOutputEnable(hdl, enable):
    """  Return current output enable state
    Args:
        hdl: the handle of opened device
        enable: LCC25 output enable state. 0:disabled,1:enabled 
    Returns:
        0: Success; negative number: failed.
    """
    en = c_int(0)
    ret = cmdGetOutputEnable(hdl, en)
    enable[0] = en.value
    return ret

def LCC25GetExternalModulation(hdl, externalmode):
    """  Return current modulation mode ¨C internal or external
    Args:
        hdl: the handle of opened device
        externalmode: LCC25 modulation mode. 0:internal modulation,1:external modulation
    Returns:
        0: Success; negative number: failed.
    """
    ex = c_int(0)
    ret = cmdGetExternalModulation(hdl, ex)
    externalmode[0] = ex.value
    return ret

def LCC25GetPreset(hdl, preset):
    """  Restore the settings saved in the preset (n)
    Args:
        hdl: the handle of opened device
        preset: n 
    Returns:
        0: Success; negative number: failed.
    """
    pre = c_int(0)
    ret = cmdGetPreset(hdl, pre)
    preset[0] = pre.value
    return ret

def LCC25GetTestModeDwellTimeMS(hdl, dwell):
    """  Return the current dwell time for LC Test Mode
    Args:
        hdl: the handle of opened device
        dwell: current dwell time(ms) 
    Returns:
        0: Success; negative number: failed.
    """
    dw = c_int(0)
    ret = cmdGetTestModeDwellTimeMS(hdl, dw)
    dwell[0] = dw.value
    return ret

def LCC25GetTestModeIncrement(hdl, increment):
    """  Return the current voltage step increment for LC Test Mode
    Args:
        hdl: the handle of opened device
        increment: current voltage step(V)
    Returns:
        0: Success; negative number: failed.
    """
    incre = c_double(0)
    ret = cmdGetTestModeIncrement(hdl, incre)
    increment[0] = incre.value
    return ret


def LCC25GetTestMinVoltage(hdl, minvoltage):
    """  Return the current starting voltage level for LC Test Mode
    Args:
        hdl: the handle of opened device
        minvoltage: current starting voltage(V)
    Returns:
        0: Success; negative number: failed.
    """
    minvol = c_double(0)
    ret = cmdGetTestMinVoltage(hdl, minvol)
    minvoltage[0] = minvol.value
    return ret

def LCC2GetTestMaxVoltage(hdl, maxvoltage):
    """  Return the current ending voltage level for LC Test Mode
    Args:
        hdl: the handle of opened device
        maxvoltage: current ending voltage(V)
    Returns:
        0: Success; negative number: failed.
    """
    maxvol = c_double(0)
    ret = cmdGetTestMaxVoltage(hdl, maxvol)
    maxvoltage[0] = maxvol.value
    return ret

def LCC25SetVoltage1(hdl, vol1):
    """ set LCC25's voltage1 value.
    Args:
        hdl: the handle of opened device
        vol: LCC25 voltage1 value, should between 0 and 25
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetVoltage1(hdl, vol1)

def LCC25SetVoltage2(hdl, vol2):
    """ set LCC25's voltage2 value.
    Args:
        hdl: the handle of opened device
        vol: LCC25 voltage1 value, should between 0 and 25
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetVoltage2(hdl, vol2)

def LCC25SetModulationFrequency(hdl, freq):
    """ set LCC25's modulation frequency(Hz)
    Args:
        hdl: the handle of opened device
        freq: LCC25 modulation frequency, should between 5 and 150
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetModulationFrequency(hdl, freq)

def LCC25SetOutputMode(hdl, mode):
    """ set LCC25's output mode
    Args:
        hdl: the handle of opened device
        mode: LCC25 output mode. 0:modulation,1:voltage1,2:voltage2 
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetOutputMode(hdl, mode)

def LCC25SetOutputEnable(hdl, enable):
    """ set LCC25's output enabled or disabled
    Args:
        hdl: the handle of opened device
        enable: 0:output is disabled,1:output is enabled
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetOutputEnable(hdl, enable)

def LCC25SetExternalModulation(hdl, mode):
    """ set LCC25 internal modulation or external modulation
    Args:
        hdl: the handle of opened device
        mode: set LCC25 internal modulation or external modulation 
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetExternalModulation(hdl, mode)

def LCC25SetPreset(hdl, preset):
    """ Store the current settings in the preset (n)
    Args:
        hdl: the handle of opened device
        preset: n 
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetPreset(hdl, preset)

def LCC25SetTestModeDwellTimeMS(hdl, dwell):
    """ Set the dwell time for LC Test Mode
    Args:
        hdl: the handle of opened device
        dwell: dwell time(ms) 
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetTestModeDwellTimeMS(hdl, dwell)

def LCC25SetTestModeIncrement(hdl, increment):
    """ Set the voltage step increment for LC Test Mode
    Args:
        hdl: the handle of opened device
        increment: voltage step increment(V)
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetTestModeIncrement(hdl, increment)

def LCC25SetTestMinVoltage(hdl, minvoltage):
    """ Set the starting voltage level for LC Test Mode
    Args:
        hdl: the handle of opened device
        voltage: starting voltage level(V)
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetTestMinVoltage(hdl, minvoltage)

def LCC25SetTestMaxVoltage(hdl, maxvoltage):
    """ Set the ending voltage level for LC Test Mode
    Args:
        hdl: the handle of opened device
        voltage: ending voltage level(V)
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetTestMaxVoltage(hdl, maxvoltage)

def LCC25SetRemote(hdl, remote):
    """ set LCC25's romote enabled or disabled
    Args:
        hdl: the handle of opened device
        remote: 0:Disable remote from being shown on display.Normal operation
  	     		1:Enable remote shown on display and display current Set voltage.Locks out buttons on from panel.
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSetRemote(hdl, remote)

def LCC25RunTestMode(hdl):
    """ Starts the LC Test Mode that will step the output voltage from the min voltage to the max voltage by steps equal to increment. 
        At each voltage level it will delay for the time specified by dwell.
    Args:
        hdl: the handle of opened device        
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdRunTestMode(hdl)

def LCC25SaveParameters(hdl):
    """ Store parameters in static memory
    Args:
        hdl: the handle of opened device        
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdSaveParameters(hdl)

def LCC25RestoreDefaultParameters(hdl):
    """ Restores the initial factory settings.
    Args:
        hdl: the handle of opened device        
    Returns: 
        0: Success; negative number: failed.
    """
    return cmdRestoreDefaultParameters(hdl)