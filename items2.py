class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. Somewhat more dangerous than a rock."
        self.damage = 20
        self.value = 20

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, but still has some fight in it."
        self.damage = 30
        self.value = 100


class Bread(Weapon):
    def __init__(self):
        self.name = "Melon Bread"
        self.description = "Slightly stale but sweet bread. Maybe you can fight an ant with it?"
        self.damage = 2
        self.health = 5
        self.value = 1

        

class PolishedSword(Weapon):
    def __init__(self):
        self.name = "Polished Sword"
        self.description = "A good, sturdy sword. Much stronger than the rusty one."
        self.damage = 150
        self.value = 500

class Excaliber(Weapon):
    def __init__(self):
        self.name = "Excaliber"
        self.description = "The cloth of the witch's item falls to reveal the legendary Excaliber sword! Use this to defeat the dragon!"
        self.damage = 100000
        self.health = 1000000
        self.value = 100000



#consumables

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+ {} HP)".format(self.name,self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60















    
# create an empty function that will pick up name, description, and damage if you pick it up when you move on a tile

