# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room, inventory=[]):
        self.name = name
        self.curr_room = curr_room
        self.inventory = inventory

    def __str__(self):
        output = ""
        output += self.name + " is in " + self.curr_room
        return output

    def move(self, direction):
        location = getattr(self.curr_room, str(f"{direction}_to"))
        if location:
            self.curr_room = location
        else:
            print("You cannot go there")

    def pick_item(self, item_name):
        self.item_name = item_name
        for i, item in enumerate(self.curr_room.items):
            if item.name.lower() == item_name:
                self.inventory.append(item)
                self.curr_room.items.remove(self.curr_room.items[i])

    def drop_item(self, item_name):
        self.item_name = item_name
        for i, item in enumerate(self.inventory):
            if item.name.lower() == item_name:
                self.curr_room.items.append(item)
                self.inventory.remove(self.inventory[i])