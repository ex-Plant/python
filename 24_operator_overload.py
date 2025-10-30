class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == 'bronze' and other.sword_type == 'bronze':
            return Sword('iron')
        if self.sword_type == 'iron' and other.sword_type == 'iron':
            return Sword('steel')

        raise Exception('cannot craft')


sword1 = Sword('bronze')
sword2 = Sword('bronze')
print((sword1 + sword2).sword_type)
