class Client:

    def __init__(self):
        self.validCommand = "showhome"

    def getValidCommand(self) -> str:
        return self.validCommand

    def execute(self, command):
        if command == "showhome":
            print("Lets show the home!")
        else:
            raise Exception("I don't know this command: " + command)
