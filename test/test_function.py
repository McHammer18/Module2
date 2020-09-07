"""
 Morgan Christensen
 Module 2 Camper Age input
 Updated: 09/07/20

 Program that takes the function from the main program
 and tests it to make sure it works
"""


import unittest
from main import CamperAgeInput


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, CamperAgeInput.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()
