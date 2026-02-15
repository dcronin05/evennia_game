from commands.command import Command
from evennia import CmdSet


class CmdEcho(Command):
    key = 'echo'

    def func(self):
        self.caller.msg(f"Echo: '{self.args}'")


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())