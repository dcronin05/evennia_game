from evennia.objects.objects import DefaultObject

class Monster(DefaultObject, name):
    key = "Monster"

    def at_init(self, name):
        print(f"{self.key} is initialized")
        self.key = name

    def move_around(self):
        print(f"{self.key} moves around")