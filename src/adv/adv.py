from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", False),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'tree':   Item("tree", "Just a tree"),
    'knife':  Item('knife', 'A very sharp knife'),
    'pig':    Item('pig', 'A wild boar'),
    'pen':    Item('pen', 'A foutain pen'),
    'bottle': Item('bottle', 'empty beer bottle'),
    'eggs':   Item('eggs', 'a dozen eggs'),
    'spoon':  Item('spoon', 'A golden spoon'),
}

treasure = {
    'gold':    Treasure('gold', '10 bars of gold', 10),
    'diamond': Treasure('diamond', '10 caret diamond', 20),
    'cash':    Treasure('cash', 'A million bucks', 30),
}

light_source = {
    'lamp':    LightSource('lamp', 'a battery lamp')
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items.extend([item['tree'], item['pig']])
room['outside'].items.extend([treasure['gold'], treasure['diamond'], treasure['cash']])
room['outside'].items.append(light_source['lamp'])
room['foyer'].items.extend([item['knife'], item['pen']])
room['overlook'].items.append(item['eggs'])
room['narrow'].items.append(item['bottle'])
room['treasure'].items.append(item['spoon'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


while(True):
    if player1.light_source_exists():
        print(player1.current_room.name)
        print(player1.current_room.description)
        print(f'Items present: {[i.name for i in player1.current_room.items]}')
    else:
        print("It's pitch black!")

    user_input = input("\nEnter command ")

    if user_input == 'q':
        break;
    print()

    player1.handle_user_input(user_input)


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    # import pdb; pdb.set_trace()
