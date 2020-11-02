from www_local_finder_cli.Command import Command
from www_local_finder_cli.Client import Client

def main():
    command = Command()

    if command.isValid():
        command = command.get()
        Client().execute(command)
    else:
        print("You missed the command")



