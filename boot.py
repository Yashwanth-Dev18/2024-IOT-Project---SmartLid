import network  # type: ignore
import utime  # type: ignore

ssid = 'Tele2_C55236'
password = 'pcdec59w'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_attempts = 20
attempts = 0

while not wlan.isconnected() and attempts < max_attempts:
    print('Connecting to network...')
    utime.sleep(1)
    attempts += 1

if wlan.isconnected():
    print('Connected to', ssid)
    print('IP address:', wlan.ifconfig()[0])
else:
    print('Failed to connect to WiFi')
