import re

class OutputInterpreterWindows:

    def is_active(self, command_output: str):

        if re.search(": active", command_output):
            return True
        elif re.search(": inactive", command_output):
            return False
        else:
            raise Exception("Command content not known. Sorry!")
    
