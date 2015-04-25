

import os

class Home(object):
    """A class to represent our home data directory, whether it exists or
    not.
    """
    ENVIRONMENT_KEY = 'DID_HOME'

    def __init__(self, environ):
        self.path = self.resolve_home_path(environ)

    def resolve_home_path(self, environ):
        home_path = '~/.did'
        if Home.ENVIRONMENT_KEY in environ:
            home_path = environ[Home.ENVIRONMENT_KEY]

        return home_path

    def ensure_exists(self):
        os.makedirs(self.path)
