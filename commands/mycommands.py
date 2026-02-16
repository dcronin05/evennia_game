from commands.command import Command
from evennia import CmdSet
from evennia import default_cmds
from evennia.utils import evmore



class Read(Command):
    """
    Read a document.

    Usage:
      read <document>
    """

    key = 'read'

    def parse_md(self, string):
        lines = string.split("\n")
        index = 0
        while index < len(lines):
            line = lines[index]

            if line == "":
                del lines[index]
                continue

            if line.startswith("# "):
                lines[index] = f"\n|*|043{line[2:]}|n\n"
            elif line.startswith("## "):
                lines[index] = f"\n|043{line[3:]}|n\n"
            elif line.startswith("### "):
                lines[index] = f"\n|C{line[4:]}|n\n"

            index += 1
        
        output = "\n" + "\n".join(lines)

        return output

    def func(self):
        if not self.args:
            self.caller.msg("Read what?")
            return
        
        document = self.caller.search(self.args)
        if not document:
            return

        text = self.parse_md(document.db.content)
        # self.caller.msg(self.parse_md(document.db.content))
        evmore.msg(caller, text, always_page=False)


class MyCmdGet(default_cmds.CmdGet):
    
    def func(self):
        super().func()
        self.caller.msg(str(self.caller.location.contents))



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
            self.weapon = weapon[0].strip()
        else:
            self.weapon = ""

    def func(self):
        if not self.target:
            self.caller.msg("Hit what?")
            return
        
        target = self.caller.search(self.target)
        if not target:
            return

        weapon = None
        if self.weapon:
            weapon = self.caller.search(self.weapon)
        if weapon:
            weaponstr = f"{weapon.key}"
        else:
            weaponstr = "bare fists"

        self.caller.msg(f"You hit {target} in the face with your {weaponstr}!")
        target.msg(f"{self.caller} hits you in the face with their {weaponstr}!")


class MyCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdEcho())
        self.add(CmdHit())
        self.add(MyCmdGet())
        self.add(Read())