from mpython import *
from bluebit import *
from machine import Timer
from umqtt.simple import MQTTClient
import ubinascii
import parrot
import time,random
import network
#��ʼģ��
st='forward'

def forward(speed=60):
	global st
    parrot.set_speed(parrot.MOTOR_1,speed)
    parrot.set_speed(parrot.MOTOR_2,speed)
    st='forward'
    oled_()

def backward(speed=60):
	global st
    parrot.set_speed(parrot.MOTOR_1,-speed)
    parrot.set_speed(parrot.MOTOR_2,-speed)
    st='backward'
    oled_()

def left(speed=600):
	global st
    parrot.set_speed(parrot.MOTOR_1,speed)
    parrot.set_speed(parrot.MOTOR_2,-speed)
    st='left'
    oled_()

def right(speed=60):
	global st
    parrot.set_speed(parrot.MOTOR_1,-speed)
    parrot.set_speed(parrot.MOTOR_2,speed)
    st='right'
    oled_()

def oled_():
    oled.fill(0)
    oled.DispChar(("״̬:"+ st),0,0,1)
    oled.show()

#������ģ��
my_wifi = wifi()

my_wifi.connectWiFi('ChinaNet-fZtZ', 'axfpkamy')#�ĳ��Լ���wifi���Ƽ�����

mqtt = MQTTClient('DFRobot/Seifer', '192.168.1.4', 1883, 'siot', 'dfrobot', keepalive=30)#ip��ַ�����Լ���

try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')

#�������Ʒ�Ӧ
def mqtt_topic_4446526f626f742f536569666572(_msg):
    if _msg == 'forward':
        forward()
    if _msg == 'backward':
        backward()
    if _msg == 'left':
        left()
    if _msg == 'right':
        right()
    if _msg == 'accelerate':
        if st=='left':
            c_speed=get_speed(motor_2)+10
            left(c_speed)
        if st=='right':
            c_speed=get_speed(motor_1)+10
            right(c_speed)
        if st=='forward':
            c_speed=get_speed(motor_2)+10
            forward(c_speed)
        if st=='backward':
            c_speed=abs(get_speed(motor_2))+10
            backward(c_speed)

    if _msg == 'backward':
        backward()

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
oled.DispChar('waiting for start',0,0)
oled.show()
while True:
    mqtt.wait_msg()

#����С��(δ��װsiri�޷���������)�����ֶ�����
forward()
oled()

#������ģ��
_dis='right'
ultrasonic = Ultrasonic()
while True:
    dis=ultrasonic.distance()
    if dis>=100:
        mqtt_topic_4446526f626f742f536569666572('accelerate')
        time.sleep(0.5)
    if dis>20 and get_speed(motor_2)==0 and get_speed(motor_1)==0:
        forward()
    if dis<=20:
        if _dis=='left':
            right()
            _dis='right'
        else:
            left()
            _dis='right'
        time.sleep(1)
    if dis<=3:
        backward()
        time.sleep(3)
