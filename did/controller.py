
from __future__ import print_function

from . import Command

class Controller(object):
    """A class to perform the correct operations on a Did datastore
    based on the command provided.
    """

    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

    def perform_command(self, command, home):
        """Accept a command object and perform the action specified on
        the datastore.
        """
        if command.has_errors():
            self._report_command_errors(command)
            return

        if command.command == Command.HELP:
            self.show_help(command, home)
        elif command.command == Command.INIT:
            self.initialize_datastore(command, home)

    def _report_command_errors(self, command):
        for error in command.errors:
            print("ERROR: " + error, file=self.stderr)

    def show_help(self, command, home):
        """Emit the help documentation to stdout.
        """
        pass

    def initialize_datastore(self, command, home):
        """Prepare our datastore if it is not already initialized.
        """
        pass
