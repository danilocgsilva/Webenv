from wwwlocalfinder.Base_Host_Finder import Base_Host_Finder
import os

class Client:

    def __init__(self):
        self.validCommand = "showhome"

    def getValidCommand(self) -> str:
        return self.validCommand

    def execute(self, command):
        if command == "showhome":
            base_host_finder = Base_Host_Finder()
            base_host_finder.set_os_name(os.name)
            print(base_host_finder.get_www_path())
        else:
            raise Exception("I don't know this command: " + command)
