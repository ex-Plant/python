class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10



wizard1 = Wizard("Gandalf", 100, 10)

print(wizard1.health)
