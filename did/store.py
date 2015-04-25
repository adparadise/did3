
class Store(object):
    """A class to represent a Did datastore.
    """

    def __init__(self, home):
        self.home = home

    def create(self):
        """Initialize this datastore
        """
        home.ensure_exists()

