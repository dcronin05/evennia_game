"""
File-based help entries. These complements command-based help and help entries
added in the database using the `sethelp` command in-game.

Control where Evennia reads these entries with `settings.FILE_HELP_ENTRY_MODULES`,
which is a list of python-paths to modules to read.

A module like this should hold a global `HELP_ENTRY_DICTS` list, containing
dicts that each represent a help entry. If no `HELP_ENTRY_DICTS` variable is
given, all top-level variables that are dicts in the module are read as help
entries.

Each dict is on the form
::

    {'key': <str>,
     'text': <str>}``     # the actual help text. Can contain # subtopic sections
     'category': <str>,   # optional, otherwise settings.DEFAULT_HELP_CATEGORY
     'aliases': <list>,   # optional
     'locks': <str>       # optional, 'view' controls seeing in help index, 'read'
                          #           if the entry can be read. If 'view' is unset,
                          #           'read' is used for the index. If unset, everyone
                          #           can read/view the entry.

"""

HELP_ENTRY_DICTS = [
    {
        "key": "evennia",
        "aliases": ["ev"],
        "category": "General",
        "locks": "read:perm(Developer)",
        "text": """
            Evennia is a MU-game server and framework written in Python. You can read more
            on https://www.evennia.com.

            # subtopics

            ## Installation

            You'll find installation instructions on https://www.evennia.com.

            ## Community

            There are many ways to get help and communicate with other devs!

            ### Discussions

            The Discussions forum is found at https://github.com/evennia/evennia/discussions.

            ### Discord

            There is also a discord channel for chatting - connect using the
            following link: https://discord.gg/AJJpcRUhtF

        """,
    },
    {
        "key": "participation05"
        "aliases": [],
        "category": "CPSI",
        "text": """
            # Discussion Assignment: Shortcuts

            Pick an application you use a lot (examples: Google Docs, Google Sheets, Microsoft Word, Adobe Premiere, VS Code, etc.). Your goal is to find and test a keyboard shortcut that helps you work faster.

            ## Steps

            - |hChoose an application|H you use frequently.
            - Find a list of keyboard shortcuts for that application.
                - Examples of what a shortcut looks like: Ctrl + C (copy), Ctrl + V (paste), Ctrl + Z (undo).
            - From that list, choose one shortcut that:
                - You have never used before
                - You think would be useful
                - No one else has already posted for that same application
            - Give it a test run (actually try it in the application).

            ## Your post

            - Application Name:
                - (What program did you try the shortcut in?)
            - Keyboard Shortcut Discovered:
                - (Exactly which keys do you press? Example: Ctrl + Shift + N)
            - What This Shortcut Does:
                - (Briefly explain the function or action this shortcut performs.)
            - Will you keep using it? Why or why not?
                - (After testing it out, do you think this shortcut will become part of your routine? Explain your reasoning.)

            ## Replies / reactions

            Replies are semi-optional, but please put at least 2 thumbs up (or similar) under shortcuts you think are worthwhile so classmates can quickly find the ones that matter.
            """,
    }
]
