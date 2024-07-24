import random
import enemies2
import npc2
import items2

#Initial tile
class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self,player):
        pass


#START tile
class StartTile(MapTile):
    def intro_text(self):
        return """
        You find youself outside, alone in a grassy meadow.
        You are the hero, looking for horrible dragon who has been plundering and burning down villages.
        Move forward to accept the quest and slay the dragon.
        """



#Additional tiles
class BoringTile(MapTile):
    def intro_text(self):
        return """
        You are walking through the grass.

        You hear a noise behind you.
        That's weird...but it's probably nothing.
        """
  
class DragonTile(MapTile):
    def __init__(self,x,y):
        self.enemy = enemies2.Dragon()
        self.alive_text = "You see the dragon opening his fire-filled mouth. Draw your weapon!"
        self.dead_text = "You defeat the dragon! Villagers swarm out and carry you on their arms. Your name will be praised as a legend."
        super().__init__(x,y)
   
    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The dragon does {} damage. You have {} HP remaining.".format(self.enemy.damage,player.hp))


            
class FinishedTile(MapTile):
    def modify_player(self,player):
        player.victory = True

    def intro_text(self):
        return """
        You've defeated the dragon!
        The village thanks you earnestly for your hard work.

        But remember, your victory comes with a price.
        The witch's voice continues to linger in your mind.
        But it's all fine...right?
        """
 

class RiverTile(MapTile):
    def intro_text(self):
        return """
        You fell into a river!
        Brr...It's freezing cold.
        Lose 5 health points
        """

    def modify_player(self,player):
        player.hp = player.hp - 5
        print("You have {} HP remaining.".format(player.hp))



class VillagerTile(MapTile):
    def intro_text(self):
        return """
        You run into a kindly old woman.
        She offers you a healing potion.
        """

    def modify_player(self,player):
        player.inventory.append(items2.HealingPotion())



class WitchTile(MapTile):

    def solution(self,player):
        witch = npc2.Witch()
        item = witch.inventory[0]
        witch.inventory.remove(item)
        player.inventory.append(item)
        print("[witch's item] accepted!")

      
    def intro_text(self):
        return """
        A woman in a cloak approaches you.
        Her voice is sweet as honey.
        She offers you a way to slay the dragon...
        ...but it comes with a price.

        Accept or forge onwards?
        """
class LuckyTile(MapTile):
    def modify_player(self,player):
        player.inventory.append(items2.PolishedSword())

    def intro_text(self):
        return """
        It's your lucky day!
        You stumbled across a [Polished Sword]!
        """

        
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc2.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError or IndexError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")
        False

    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """

#FIND gold
class FindGoldTile(MapTile):
    def __init__(self,x,y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x,y)

    def modify_player(self,player):
        if not self.gold_claimed:
            self.gold_claimed = True
        player.gold = player.gold + self.gold
        print("+{}gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable part of the valley. You must forge onwards.
            """
        else:
            return """
            Someone dropped some gold. You pick it up.
            """


#Add enemies
class EnemyTile(MapTile):
    def __init__(self,x,y):
        r = random.random()
        #ADD Giant Spider
        if r < 0.5:
            self.enemy = enemies2.GiantSpider()
            self.alive_text = "A giant spider jumps down from its web in front of you!"
            self.dead_text = "The corpse of a dead spider rots on the ground."

        #ADD Ogre
        elif r < 0.8:
            self.enemy = enemies2.Ogre()
            self.alive_text = "An ogre is blocking your path."
            self.dead_text = "A dead ogre reminds you of your triumph."

        #ADD Bat Colony
        elif r < 0.95:
            self.enemy = enemies2.BatColony()
            self.alive_text = "You hear a squeaking noise growing louder."\
                              "...suddenly you are lost in a swarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."

        #ADD Rock Monster
        else:
            self.enemy = enemies2.RockMonster()
            self.alive_text = "You've disturbed a rock monster."
            self.dead_text = "Defeated, the monster has reverted into an ordinary rock."
        super().__init__(x,y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage,player.hp))



#initiate world
world_dsl = """
|  |  |FT|  |  |  |
|WT|EN|DT|EN|VT|BT|
|EN|VT|VT|RT|RT|EN|
|EN|FG|EN|BT|LT|VT|
|FG|TT|EN|VT|BT|EN|
|BT|VT|ST|FG|TT|BT|
|FG|BT|FG|EN|VT|RT|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|DT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

tile_type_dict = {"DT": DragonTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "RT": RiverTile,
                  "VT": VillagerTile,
                  "WT": WitchTile,
                  "BT": BoringTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "FT": FinishedTile,
                  "LT": LuckyTile,
                  "  ": None}
world_map = []
start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate (dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate (dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x,y
            row.append(tile_type(x,y) if tile_type else None)

        world_map.append(row)
    


def tile_at(x,y):
    if x<0 or y<0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None










