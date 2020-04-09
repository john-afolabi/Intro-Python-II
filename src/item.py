class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f"{self.name} was picked up"

    def on_drop(self):
        return f"{self.name} was dropped"