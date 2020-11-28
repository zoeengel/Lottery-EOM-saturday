# ZOE ENGEL, CLASS 1

# CREATING A UNIT TEST FOR THE LOTTERY TASK
import unittest
class TestAge(unittest.TestCase):
    def testentries(self):

        x= 900
        message="False"
        self.assertIn(x, range(1, 100), message)
