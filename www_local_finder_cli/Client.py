from wwwlocalfinder.Base_Host_Finder import Base_Host_Finder
from www_local_finder_cli.Diagnose import Diagnose
import os

class Client:

    def __init__(self):
        self.validCommands = ["showhome", "diagnose"]

    def getValidCommands(self) -> str:
        return self.validCommands

    def execute(self, command):
        if command == "showhome":
            base_host_finder = Base_Host_Finder()
            base_host_finder.set_os_name(os.name)
            print(base_host_finder.get_www_path())
        elif command == "diagnose":
            diagnose = Diagnose()
            diagnose.apache()
            diagnose.mysql()
        else:
            raise Exception("I don't know this command: " + command)
