from time import sleep

class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
             print('\033[31m Красный')
             sleep(7)
             print('\033[33m Желтый')
             sleep(2)
             print('\033[32m Зеленый')
             sleep(7)
             print('\033[33m Желтый')
             sleep(2)

trafficlight = TrafficLight()
trafficlight.running()