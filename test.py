import unittest
from Lottery_App import *

class agetest(unittest.TestCase):
    from Lottery_App import validate
    def age(self):
        x = validate()
        msg = 'false'
        self.assertIn(x, range(1,99), msg)
