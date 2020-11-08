import os
from www_local_finder_cli.PosixCommands import PosixCommands
from www_local_finder_cli.WindowsCommands import WindowsCommands

class OsCommands:

    def __init__(self, osname):
        if osname == "posix" or osname == "darwin":
            self.oscommand = PosixCommands()
        elif osname == "nt":
            self.oscommand = WindowsCommands()
        else:
            raise Exception("Sorry! I don't know ehich is this system!")

    def command_check_apache(self) -> str:
        return self.oscommand.command_check_apache()

    def command_check_mysql(self) -> str:
        return self.oscommand.command_check_mysql()
