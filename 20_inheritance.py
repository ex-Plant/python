# Assignment
# Complete the following methods:
#
# Complete the unit's in_area method. It accepts an "area" represented by four points: x_1, y_1, x_2, and y_2. The coordinates x_1 and y_1 represent the bottom-left corner, while x_2 and y_2 represent the top-right corner.
# Determine if the unit is within the given area by using the unit's position coordinates pos_x and pos_y.
# Return True if the unit's position falls inside or on the edge of the rectangle. Otherwise, return False.
# Complete the dragon's breathe_fire method. It causes the dragon to breathe a swath of fire at the target area.
# The target area is centered at (x, y). The area stretches for __fire_range in both directions inclusively.
# Iterate over each unit in the units list, and check if the unit is in the area. If it is, add it to a new list that keeps track of the units hit by the blast.
# Return the list of units hit by the blast.

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
          self.pos_y >= y_1
          and self.pos_y <= y_2
          and self.pos_x >= x_1
          and self.pos_x <= x_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_affected_by_dragon_fire = []
        area_x_1 = x - self.__fire_range
        area_x_2 = x + self.__fire_range
        area_y_1 = y - self.__fire_range
        area_y_2 = y + self.__fire_range

        for unit in units:
            if unit.in_area(area_x_1, area_y_1, area_x_2, area_y_2 ):
                units_affected_by_dragon_fire.append(unit)

        return units_affected_by_dragon_fire
