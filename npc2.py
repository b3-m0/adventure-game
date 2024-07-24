import items2

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name



class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader Joe"
        self.gold = 100
        self.inventory = [items2.CrustyBread(), items2.CrustyBread(), items2.CrustyBread(), items2.HealingPotion(), items2.HealingPotion()]

class Witch(NonPlayableCharacter):
    def __init__(self):
        self.name = "Witch"
        self.inventory = [items2.Excaliber()]

