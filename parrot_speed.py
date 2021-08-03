#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parrot_speed.py
#  
#  Copyright 2021 此间兮若流年 <此间兮若流年@LAPTOP-541EAAFT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  

#导入库
from mython import *
from bluebit import *
import parrot
import time

cmd = True
speed = 50											#初始速度设为50，正转
def speed_commond(speed):
	if cmd = True:									#如果为真，则提高速度，每次改变10
		try:
			speed = speed + 10
		except:
			pass
	else:
		try:
			speed = speed - 10
		except:
			pass                        
def parrot_left(speed):
	"""控制左转"""
	m1_speed =-speed
	m2_speed = speed
	parrot.set_speed(parrot.MOTOR_1,m1_speed)       #  设置m1反转
	parrot.set_speed(parrot.MOTOR_2,m2_speed)       #  设置m2正转
	
def parrot_right(speed):
	"""控制右转"""
	m1_speed = speed
	m2_speed =-speed
	parrot.set_speed(parrot.MOTOR_1,m1_speed)       #  设置m1正转
	parrot.set_speed(parrot.MOTOR_2,m2_speed)       #  设置m2反转
