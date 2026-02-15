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

    def parse(self):
        self.args = self.args.strip()
        target, *weapon = self.args.split(" with ", 1)
        if not weapon:
            target, *weapon = target.split(" ", 1)
        self.target = target.strip()
        if weapon:
            self.weapon = weapon.strip()
        else:
            self.weapon = ""

    def func(self):
        if not self.target:
            self.caller.msg("Hit what?")
            return
        
        target = self.caller.search(self.target)
        if not target:
            return

        if self.weapon:
            weapon = self.caller.search(self.weapon)
        if weapon:
            weaponstr = f"{weapon.key}"
        else:
            weaponstr = "bare fists"

        self.caller.msg(f"You hit {target} in the face with their {weaponstr}!")
        target.msg(f"{self.caller} hits you in the face with their {weaponstr}!")


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())
        self.add(CmdHit())