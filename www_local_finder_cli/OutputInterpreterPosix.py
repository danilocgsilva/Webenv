import re

class OutputInterpreterPosix:

    def is_active(self, command_output):

        command_output_string = command_output.decode("utf-8")
        command_results_splited = command_output_string.split("\n")
        line_to_check = command_results_splited[2]

        if re.search(": active", line_to_check):
            return True
        return False
