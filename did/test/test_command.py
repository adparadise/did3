

import unittest

from did import Command

class TestCommand(unittest.TestCase):

    def test_consume_blank(self):
        command = Command()
        command.consume_argv(['bin/did'])

        self.assertEqual(command.command, Command.HELP)


if __name__ == '__main__':
    unittest.main()
