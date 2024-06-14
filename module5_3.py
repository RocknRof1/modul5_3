class Building:
    def __init__(self, name, floor):
        self.namberOfFloor = floor
        self.buildingType = name

    def __eg__(self, other):
        return self.buildingType == other.buildingType and self.namberOfFloor == other.numberOfFloor

a1 = Building('ЖК Лесная тропа', 12)
a2 = Building('Урицкого стайл', 86)
a3 = Building('Кострома тревел', 8)
print(a1 == a2)
print(a1 == a3)