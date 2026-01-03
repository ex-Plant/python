class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.effciency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_spped, efficiency)
        self.load_weight = load_weight
        self.bed_area + bed_area

    def get_trip_cost(self, distance, food_price):
        pass

    def get_cargo_volume(self):
        pass


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        pass

    def get_cargo_volume(self):
        pass
