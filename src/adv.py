from room import Room
from player import Player
from item import Item
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

room["outside"].items.append(Item("Book", "An old dusty book"))

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

divider = "\n-----------------------------------\n"
running = True

playername = input(divider + "Welcome!!!" + divider +
                   "Enter your player name: ")

if (playername):
    while running:
        player = Player(playername, room['outside'])
        print(f"\nHi {playername}\n")
        print("What do you want to do?")
        print("     N: to move North")
        print("     S: to move South")
        print("     E: to move East")
        print("     W: to move West")
        print("     I: to see Inventory")
        print("     L: to look Around")
        print("     Q: to Quit")
        option = input("Select an option: ").lower()

        cmd = option.split()

        if len(cmd) == 1:
            if cmd[0] in ["n", "s", "e", "w"]:
                player.move(cmd[0])
            elif cmd[0] == "l":
                player.look_around()
            elif cmd[0] == "i":
                player.check_inventory()
            elif cmd[0] == "q":
                print(divider + "Goodbye !!" + divider)
                break
            else:
                print(divider + "Invalid Input" + divider)

        if len(cmd) == 2:
            pick_verbs = ["pick", "get", "take"]
            drop_verbs = ["drop", "use"]

            if cmd[0] in pick_verbs:
                player.pick_item(cmd[1])
            elif cmd[0] in drop_verbs:
                player.drop_item(cmd[1])
            else:
                print(divider + "You entered an Invalid action" + divider)
