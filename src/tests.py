from app import fizz_buzz 
import unittest

"""
Unit Tests that cover all code-paths of the fizz_buzz function
"""
class FizzBuzzTest(unittest.TestCase):
    def test_multiple_of_three(self):
        self.assertEqual(fizz_buzz(3), 'Devhaus')
    
    def test_multiple_of_five(self):
        self.assertEqual(fizz_buzz(5), 'Learning')
    
    def test_multiple_of_seven(self):
        self.assertEqual(fizz_buzz(7), 'Model')

    def test_multiple_of_three_five(self):
        self.assertEqual(fizz_buzz(15), 'Devhaus Learning')

    def test_multiple_of_three_seven(self):
        self.assertEqual(fizz_buzz(21), 'Devhaus Model')

    # Ensure the case of 5 takes precedence over the case of 7
    def test_multiple_of_five_seven(self):
        self.assertEqual(fizz_buzz(35), 'Learning')

    def test_multiple_of_three_five_seven(self):
        self.assertEqual(fizz_buzz(105), 'Devhaus Learning Model')

    def test_none(self):
        self.assertEqual(fizz_buzz(1), '1')

if __name__ == '__main__':
    unittest.main()
    