class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10



wizard1 = Wizard("Gandalf", 100, 10)
print(wizard1.health)

class Wizard2:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self, fireball_damage):
        self.health -= (fireball_damage - self.__stamina)

    def drink_mana_potion(self, potion_mana):
        self.mana += (potion_mana + self.__intelligence)


class Wizard3:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if fireball_cost > self.mana:
            raise Exception(f'{self.name} cannot cast fireball')
        self.mana -= fireball_cost
        target.get_fireballed(fireball_damage)

    def is_alive(self):
        return self.health > 0

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.____account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")

        self.__balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")

        if self.__balance < amount:
            raise ValueError("insufficient funds")

        self.__balance -= amount

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed


    def get_position(self):
        return self.__pos_x, self.__pos_y
