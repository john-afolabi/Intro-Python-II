from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
playername = input(
    "\n************\nWelcome!!!\n************\nEnter your player name: ")

if (playername):
    player = Player(playername, room['outside'])
    # Write a loop that:
    #
    while True:
        # * Prints the current room name
        if player.curr_room:
            print(
                f"\nYou are in the {player.curr_room.name}\n{player.curr_room.description}"
            )
        else:
            print('You cannot go in that direction')
        if len(player.curr_room.items) > 0:
            print("\n The following items are in the room:")
            for item in player.curr_room.items:
                print(f"\n{item.name}")
        # * Waits for user input and decides what to do.
        option = input(
            f"\nWhat direction are you going {player.name}?\nEnter:\n   N for North\n   S for South\n   E for East\n   W for West: "
        ).lower()
        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        if option in ["n", "s", "e", "w"]:
            player.move(option)
        elif option == "q":
            print(f"\n************\nGoodbye {playername}\n************")
            break
        else:
            print("\n************\nInvalid input\n************\n")

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
