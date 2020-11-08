import re

class OutputInterpreterWindows:

    def is_active(self, command_output):

        command_output_string = command_output.decode("windows-1252")
        command_results_splited = command_output_string.split("\r\n")
        line_to_check = command_results_splited[3]

        if re.search("RUNNING", line_to_check):
            return True
        return False
