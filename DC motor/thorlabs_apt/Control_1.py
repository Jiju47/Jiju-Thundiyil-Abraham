# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 23:54:08 2021

@author: jiju4
"""

import thorlabs_apt as apt

def main():
    
    apt.list_available_devices()
    [(50, 55000038)]
    motor = apt.Motor(83854555)
    motor.move_home(True)
    motor.set_hardware_limit_switches(1, 1)
    
    motor.move_by(45)
    
    print("flag 1")
main()