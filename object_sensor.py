from machine import Pin  # type: ignore
import time

object_sensor = Pin(28, Pin.IN, Pin.PULL_DOWN)

while True:
    # 物体を検知したら、ON
    if object_sensor.value() == 1:
        print("Object detected")

    # 物体を検知しなかったら、OFF

    elif object_sensor.value() == 0:
        print("Object not detected")

    # エラー
    else:
        print("Error")

    time.sleep(0.1)
