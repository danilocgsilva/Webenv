import sys
from www_local_finder_cli.Client import Client

class Command:

    def __init__(self):
        try:
            if sys.argv[1] in Client().getValidCommands():
                self.validity = True
                self.command = sys.argv[1]
            else:
                self.validity = False
                self.command = ""
        except IndexError:
            self.validity = False
            self.command = ""

    def isValid(self) -> bool:
        return self.validity

    def get(self):
        return self.command
