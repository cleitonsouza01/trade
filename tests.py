from __future__ import absolute_import

import os, sys, inspect
import unittest

from tests import *

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


if __name__ == '__main__':
    unittest.main()
