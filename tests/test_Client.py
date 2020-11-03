import unittest
import sys
sys.path.insert(1, "..")
from www_local_finder_cli.Client import Client
from unittest.mock import patch

class test_Client(unittest.TestCase):

    def test_exception_invalid_command(self):
        client = Client()
        with self.assertRaises(Exception):
            client.execute("this_command_does_not_exists")
