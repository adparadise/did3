import os
import sys
import inspect

class PathManager(object):
    """A class to manage our import path so that our project is
    included.
    """

    def __init__(self, currentframe):
        self.currentframe = currentframe

    def get_project_home(self):
        """Find the absolute path to this project so we can import files
        from it.
        """
        relative_filename = inspect.getfile(self.currentframe)
        absolute_filename = os.path.abspath(relative_filename)
        bin_home = os.path.dirname(absolute_filename)
        project_home = os.path.join(bin_home, '..')
        project_home = os.path.realpath(project_home)

        return project_home

    def include_project_home(self):
        """Include this project in the import search paths.
        """
        project_home = self.get_project_home()
        sys.path.insert(0, project_home)

