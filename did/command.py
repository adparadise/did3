

class Command(object):
    """A class to represent the command requested by the user as
    defined by the inputs they typed.
    """

    HELP = 'help'
    INIT = 'init'

    def __init__(self):
        self.errors = []

    def consume_argv(self, argv):
        """Accept the arguments as found in sys.argv, altering this
        instance to represent the requested command.
        """

        self.command = Command.HELP
        if len(argv) >= 2:
            self.command = argv[1]

        if Command.HELP == self.command:
            self._consume_init_argv(argv)
        elif Command.INIT == self.command:
            self._consume_help_argv(argv)
        else:
            self.errors.append('no such command: ' + self.command)

    def has_errors(self):
        return len(self.errors) > 0

    def _consume_help_argv(self, argv):
        """Gather arguments indicating what help to show
        """
        pass

    def _consume_init_argv(self, argv):
        """Build up the arguments as related to the init command
        """
        pass
