#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parrot_speed.py
#  
#  Copyright 2021 �˼��������� <�˼���������@LAPTOP-541EAAFT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  

#�����
from mython import *
from bluebit import *
import parrot
import time

cmd = True
speed = 50											#��ʼ�ٶ���Ϊ50����ת
def speed_commond(speed):
	if cmd = True:									#���Ϊ�棬������ٶȣ�ÿ�θı�10
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
	"""������ת"""
	m1_speed =-speed
	m2_speed = speed
	parrot.set_speed(parrot.MOTOR_1,m1_speed)       #  ����m1��ת
	parrot.set_speed(parrot.MOTOR_2,m2_speed)       #  ����m2��ת
	
def parrot_right(speed):
	"""������ת"""
	m1_speed = speed
	m2_speed =-speed
	parrot.set_speed(parrot.MOTOR_1,m1_speed)       #  ����m1��ת
	parrot.set_speed(parrot.MOTOR_2,m2_speed)       #  ����m2��ת
