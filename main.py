import machine  # type: ignore
from machine import Pin, PWM  # type: ignore
import utime  # type: ignore
import urequests as requests  # type: ignore


trigger = machine.Pin(2, machine.Pin.OUT)
echo = machine.Pin(3, machine.Pin.IN)
servo = machine.Pin(1)
pwm = machine.PWM(servo)
pwm.freq(50)

# UBIDOT SETUP
TOKEN = "BBUS-8yF1VY42uoq9fySuVCSmgQQ7ctdo4o"
DEVICE_LABEL = "picolid"
count_VAR = "count"
avg_VAR = "avgdist"
dist_VAR = "distance"

count = 0
AVG_dist = 0.0
distance = 0
start_time = utime.time()


def measure_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()

    timepassed = signalon - signaloff  # type: ignore
    distance = (timepassed * 0.0343) / 2
    return distance


def build_json(count_variable, count_value, distance_variable, distance_value,
               avg_distance_variable, avg_distance_value):
    try:
        data = {
            count_variable: {"value": count_value},
            avg_distance_variable: {"value": avg_distance_value},
            distance_variable: {"value": distance_value}
        }
        return data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def send_data(device, count_variable, count_value, distance_variable,
              distance_value, avg_distance_variable, avg_distance_value):
    try:
        url = "https://industrial.api.ubidots.com/api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

        data = build_json(count_variable, count_value, distance_variable,
                          distance_value, avg_distance_variable,
                          avg_distance_value)

        if data is not None:
            # print("Sending data to Ubidots:", data)
            req = requests.post(url=url, headers=headers, json=data)
            # print("Response from Ubidots:", req.json())
            req.close()
        else:
            print("Error: Data is None")
    except Exception as e:
        print("Error sending data:", e)


try:
    while True:
        # Get the current time
        current_time = utime.localtime()
        current_hour = current_time[3]

        # Checking if it's midnight (00:00:00)
        # 00:00:00 to 00:00:59
        if current_hour == 0 and current_time[4] == 0 and current_time[5] < 1:
            # Reset count and AVG_dist
            count = 0
            AVG_dist = 0
            print("Midnight reached, variables reset.")

        distance = measure_distance()

        if 0 < distance < 30:
            count += 1
            AVG_dist += distance
            AVG_dist = AVG_dist/count
            print("Object detected! Distance:", distance, "cm")

            led = Pin("LED", Pin.OUT)
            led.on()
            MIN = 1000000
            MAX = 2000000
            pwm = PWM(Pin(0))
            pwm.freq(50)
            pwm.duty_ns(MAX)
            utime.sleep(2.5)
            pwm.duty_ns(MIN)
            led.off()
            send_data(DEVICE_LABEL, count_VAR, count, avg_VAR, AVG_dist,
                      dist_VAR, distance)
        utime.sleep(0.1)

except KeyboardInterrupt:
    pwm.deinit()
    print("Program stopped")
