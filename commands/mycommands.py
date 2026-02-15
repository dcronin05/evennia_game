from commands.command import Command
from evennia import CmdSet


class CmdEcho(Command):
    """
    Echo the arguments back to the |Rcaller|n.
    """

    key = 'echo'

    def func(self):
        self.caller.msg(f"Echo: '{self.args.strip()}'")


class CmdHit(Command):
    """
    Hit a target.

    Usage:
      hit <target>
    """

    key = 'hit'

    def func(self):
        args = self.args.strip()
        if not args:
            self.caller.msg("Hit what?")
            return
        
        target = self.caller.search(args)
        if not target:
            return
        self.caller.msg(f"You hit {target} in the face!")
        target.msg(f"{self.caller} hits you in the face!")


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())
        self.add(CmdHit())