# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room

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
