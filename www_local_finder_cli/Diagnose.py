import subprocess
import re

class Diagnose:

    def apache(self):
        self.__check_running("Apache", ["service", "apache2", "status"])

    def mysql(self):
        self.__check_running("Mysql", ["service", "mysql", "status"])

    def __check_running(self, service, command_to_check):
        content_output = self.__getContentFromCommand(command_to_check)
        if re.search(": active", content_output):
            print(service + " is running")
        elif re.search(": inactive", content_output):
            print(service + " is down")

    def __getContentFromCommand(self, command_list: list):
        ps = subprocess.Popen(command_list, stdout=subprocess.PIPE)
        output = subprocess.check_output(("grep", "-i", "active"), stdin=ps.stdout)
        return output.decode("utf-8")