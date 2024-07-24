from collections import OrderedDict
from player2 import Player
import world2



def play():
    print("Slay the dragon!")
    world2.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world2.tile_at(player.x,player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room,player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")


def choose_action(room,player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")

def get_available_actions(room,player):
    actions = OrderedDict()
    print("Choose an action: ")

    if player.inventory:
        action_adder(actions, 'i',player.print_inventory, "Print inventory")

    if isinstance(room,world2.TraderTile):
        action_adder(actions,'t',player.trade,"Trade")

    if isinstance(room,world2.WitchTile):
        action_adder(actions,'a',player.witch,"Accept")

    if isinstance(room, world2.DragonTile) and room.enemy.is_alive():
        action_adder(actions,'a',player.attack,"Attack")

    if isinstance(room, world2.EnemyTile) and room.enemy.is_alive():
        action_adder(actions,'a',player.attack,"Attack")

    else:
        if world2.tile_at(room.x,room.y-1):
            action_adder(actions,'n',player.move_north,"Go north")
        if world2.tile_at(room.x,room.y+1):
            action_adder(actions,'s',player.move_south,"Go south")
        if world2.tile_at(room.x + 1,room.y):
            action_adder(actions,'e',player.move_east,"Go east")
        if world2.tile_at(room.x - 1,room.y):
            action_adder(actions,'w',player.move_west,"Go west")

    if player.hp < 100:
        action_adder(actions,'h',player.heal,"Heal")

    return actions

def action_adder(action_dict,hotkey,action,name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey,name))


  
play()


