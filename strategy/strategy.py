from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, attacker, opponent):
        pass

class Thunderbolt(AttackStrategy):
    def attack(self, attacker, opponent):
        print(attacker.name + " used Thunderbolt!")
        opponent.health -= 40
        print(opponent.name + "'s health is now " + str(opponent.health) + " HP")

class Flamethrower(AttackStrategy):
    def attack(self, attacker, opponent):
        print(attacker.name + " used Flamethrower!")
        opponent.health -= 50
        print(opponent.name + "'s health is now " + str(opponent.health) + " HP")

class Pokemon(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self, opponent):
        pass

class Pikachu(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.attack_strategy = Thunderbolt()

    def attack(self, opponent):
        self.attack_strategy.attack(self, opponent)

class Charmander(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.attack_strategy = Flamethrower()
    
    def attack(self, opponent):
        self.attack_strategy.attack(self, opponent)

def main():
    pikachu = Pikachu("Pikachu", 100)
    charmander = Charmander("Charmander", 95)

    pikachu.attack(charmander)
    charmander.attack(pikachu)

if __name__ == '__main__':
    main()