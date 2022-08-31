# boot.py -- run on boot-up
import network
import uos
import machine

# import wifi_credentials form SD Card
uos.mount(machine.SDCard(), "/sd")
led = machine.Pin(4, machine.Pin.OUT)
led.off()


ssid = ''
password = ''

wifi_credentials = open('wifi_credentials.txt', 'r')

count = 0
for line in wifi_credentials:
    if line.startswith('ssid:'):
        ssid = line.rstrip()

    elif line.startswith('password:'):
        password = line.rstrip()
        
    count += 1

ssid = ssid[5:]
password = password[9:]


def do_connect():
    print('ssid: ' + ssid)
    print('password: ' + password)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
