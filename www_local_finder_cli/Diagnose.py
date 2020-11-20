from www_local_finder_cli.OsCommands import OsCommands
from www_local_finder_cli.OutputInterpreterPosix import OutputInterpreterPosix
from www_local_finder_cli.OutputInterpreterWindows import OutputInterpreterWindows
import subprocess
import re
import os

class Diagnose:

    def __init__(self):
        self.oscommands = OsCommands(os.name)
        if os.name == "posix" or os.name == "darwin":
            self.interpreter = OutputInterpreterPosix()
        elif os.name == "nt":
            self.interpreter = OutputInterpreterWindows()
        else:
            raise Exception("Sorry! I don't know witch is this system!")

    def apache(self):
        self.__check_running("Apache", self.oscommands.command_check_apache().split(" "))

    def mysql(self):
        self.__check_running("Mysql", self.oscommands.command_check_mysql().split(" "))

    def docker(self):
        command = ["systemctl", "is-active", "docker"]
        FNULL = open(os.devnull, 'w')
        try:
            result = subprocess.check_output(command)
            result_string = result.decode("utf-8").replace("\n", "")
            if result_string == "active":
                print("Docker is running")
            else:
                print("Docker is not running")
        except subprocess.CalledProcessError as e:
            print("Docker is not running")

    def __check_running(self, service, command_to_check):
        process = subprocess.Popen(command_to_check, stdout=subprocess.PIPE)
        stdoutbytes, err = process.communicate()
        if self.interpreter.is_active(stdoutbytes):
            print(service + " is running")
        else:
            print(service + " is down")

    def __is_active(self, command_output: str):
        if re.search(": active", command_output):
            return True
        elif re.search(": inactive", command_output):
            return False
        else:
            raise Exception("Command content not known. Sorry!")
