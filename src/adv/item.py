class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        pass

    def on_drop(self, player = None):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.has_been_picked_up = False

    def on_take(self, player):
        if not self.has_been_picked_up:
            self.has_been_picked_up = True
            player.score += self.value

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self, player = None):
        print('It is not wise for you to drop your source of light!')


