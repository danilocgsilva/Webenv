import os
from www_local_finder_cli.PosixCommands import PosixCommands
from www_local_finder_cli.WindowsCommands import WindowsCommands

class OsCommands:

    def __init__(self, osname):
        if osname == "posix" and osname == "darwin":
            self.oscommand = PosixCommands()
        elif osname == "nt":
            self.oscommand = WindowsCommands()

    def command_check_apache(self) -> str:
        return self.oscommand.command_check_apache()

    def command_check_mysql(self) -> str:
        return self.oscommand.command_check_mysql()
