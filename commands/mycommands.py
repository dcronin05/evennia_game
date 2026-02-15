from commands.command import Command
from evennia import CmdSet


class CmdEcho(Command):
    key = 'echo'


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())