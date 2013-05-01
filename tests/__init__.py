"""
from .cases import *
"""

import unittest

from . import youtube

suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(youtube.TestCase),
])

def run():
    return unittest.TextTestRunner(verbosity=2).run(suite)

