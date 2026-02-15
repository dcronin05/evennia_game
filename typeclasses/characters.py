"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

import random

from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character just re-implements some of the Object's methods and hooks
    to represent a Character entity in-game.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Object child classes like this.

    """

    def at_object_creation(self):
        super().at_object_creation()
        self.db.strength = random.randint(10, 22)
        self.db.dexterity = random.randint(10, 22)
        self.db.intelligence = random.randint(10, 22)
    
    def get_stats(self):
        """
        Returns the stats of the character.
        """
        return self.db.strength, self.db.dexterity, self.db.intelligence


class God(Character):
    """
    God class
    """

    def at_object_creation(self):
        super().at_object_creation()
        self.db.strength = 30
        self.db.dexterity = 30
        self.db.intelligence = 30
