# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 23:54:08 2021

@author: jiju4
"""

from pylablib.devices import Thorlabs



print("flag1")

Thorlabs.list_kinesis_devices()


from pylablib.devices import Thorlabs

Thorlabs.list_kinesis_devices()
stage = Thorlabs.KinesisMotor("83847373")
stage.blink()
# LED of the motor blinks
stage.home()

stage._move_by()
# motor move 0.5 degree when stage._move_by(1000) command is given
stage._move_to()
# motor move to 1 degree when 1923 is put in the bracket
stage._jog(1)
# Moves clk wise
stage._jog(0)
#Moves anti clk wise