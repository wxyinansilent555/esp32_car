#mPythonType:0
from mpython import *
from machine import Timer
import ubinascii
import time
import network

my_wifi = wifi()

my_wifi.connectWiFi('TP-LINK_F902', 'ls2528379')

from umqtt.simple import MQTTClient

mqtt = MQTTClient('DFRobot/Seifer', '192.168.1.101', 1883, 'siot', 'dfrobot', keepalive=30)

try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')

def mqtt_topic_4446526f626f742f536569666572(_msg):
    if _msg == 'on':
        rgb[0] = (int(255), int(0), int(0))
        rgb.write()
        time.sleep_ms(1)

def mqtt_callback(topic, msg):
    try:
        topic = topic.decode('utf-8', 'ignore')
        _msg = msg.decode('utf-8', 'ignore')
        eval('mqtt_topic_' + bytes.decode(ubinascii.hexlify(topic)) + '("' + _msg + '")')
    except: print((topic, msg))

mqtt.set_callback(mqtt_callback)

mqtt.subscribe("DFRobot/Seifer")

def timer14_tick(_):
    mqtt.ping()

tim14 = Timer(14)
tim14.init(period=20000, mode=Timer.PERIODIC, callback=timer14_tick)
oled.fill(0)
oled.DispChar('Connected', 0, 0)
oled.DispChar(my_wifi.sta.ifconfig()[0], 0, 16, 1)
oled.show()
while True:
    mqtt.wait_msg()
