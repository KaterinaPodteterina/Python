class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight (self):
        return f"Необходимая масса асфальта {(self._length * self._width * 25 * 5)} т"

road_1 = Road(1000, 30)
print (road_1.road_weight())
