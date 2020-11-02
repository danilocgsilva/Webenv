import sys
from www_local_finder_cli.Client import Client

class Command:

    def __init__(self):
        try:
            if sys.argv[1] == "showhome":
                self.command = sys.argv[1]
            else:
                self.command = ""
        except IndexError:
            self.command = ""

    def isValid(self) -> bool:
        if self.command == Client().getValidCommand():
            return True
        return False

    def get(self):
        return self.command
