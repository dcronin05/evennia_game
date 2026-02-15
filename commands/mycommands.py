from commands.command import Command
from evennia import CmdSet


class CmdEcho(Command):
    key = 'echo'
    help_category = 'Fun'

    
class MyCmdSet(CmdSet):
    key = 'my_cmd_set'
    priority = 10

    def at_cmdset_creation(self):
        self.add(CmdEcho())