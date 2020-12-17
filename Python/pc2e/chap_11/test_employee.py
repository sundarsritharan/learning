import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ test all aspects of Employee class """

    def setUp(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_raise()
        print(self.eric.salary)
        self.assertEqual(self.eric.first_name, 49494)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

    if __name__ == '__main__':
        unittest.main()