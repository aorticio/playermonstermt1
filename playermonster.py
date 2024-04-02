class Entity:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
    
    def attack(self, target):
        if self.is_alive() == True:
            if target.is_alive() == True:
                target.take_damage = self.__attack_power
                print(f'{self.__name} dealt {self.__attack_power} to {target.__name}')
                print(target.take_damage)
                print(f'{target.__name} health: {target.__health}')
            else:
                print(f'{target.__name} is dead')
        else:
            print(f'{target.name} no enemy')
    
    @property
    def take_damage(self):
        return self.__health
    
    @take_damage.setter
    def take_damage(self, attack_power):
        self.__health -= attack_power

    def is_alive(self):
        if self.__health <= 0:
            return False
        else:
            return True

class Player(Entity):
    def __init__(self, name: str, health: int, attack_power: int) -> None:
      super().__init__(name, health, attack_power)
    
    
class Monster(Entity):
    def __init__(self, name: str, health: int, attack_power: int) -> None:
      super().__init__(name, health, attack_power)
    

player1 = Player(name='P1', health = 75, attack_power= 75)
monster1 = Monster(name='Bear', health = 50, attack_power=25)

monster1.attack(player1)
# print(monster1)
print(player1.take_damage)