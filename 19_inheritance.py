class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class ArcherHero(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows < 1:
            raise Exception('not enough arrows')
        self.__num_arrows -= 1
        target.take_damage(10)


class WizardHero(Hero):
    def __init__(self, name, health, mana):
      super().__init__(name, health)
      self.__mana= mana

    def cast(self, target):
      if self.__mana < 25:
        raise Exception('not enough mana')
      target.take_damage(25)
      self.__mana =- 25
      print('target health after attack', target.get_health() ) # 225


h = WizardHero("Gandalf", 200, 1000)
enemy = WizardHero("Saruman", 250, 500)

h.cast(enemy)
