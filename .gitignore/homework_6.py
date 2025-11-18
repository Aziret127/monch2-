class Distance:
    conversion_dict = {
        "мм": 0.001,
        "см": 0.01,
        "м": 1,
        "км": 1000,
    }

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit.lower()

    def __str__(self):
        return f"Distance object, value={self.value} unit={self.unit}"

    def to_meters(self):
        return self.value * Distance.conversion_dict[self.unit]

    @staticmethod
    def from_meters(value_in_meters, target_unit):
        coef = Distance.conversion_dict[target_unit]
        return Distance(value_in_meters / coef, target_unit)

    def __add__(self, other):
        # просто предполагаем, что other — объект Distance
        total_meters = self.to_meters() + other.to_meters()
        return Distance.from_meters(total_meters, self.unit)

    def __sub__(self, other):
        total_meters = self.to_meters() - other.to_meters()
        return Distance.from_meters(total_meters, self.unit)

d1 = Distance(10, "м")
d2 = Distance(2, "км")
d3 = Distance(150, "см")

print(d1)
print(d2)
print(d3)

print(d1 + d2)
print(d3 + d1)

print(d2 - d1)
print(d1 - d3)

