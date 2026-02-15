from commands.command import Command
from evennia import CmdSet


class CmdEcho(Command):
    """
    Echo the arguments back to the |Rcaller|n.
    """

    key = 'echo'

    def func(self):
        self.caller.msg(f"Echo: '{self.args.strip()}'")


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())