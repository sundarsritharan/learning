# test city names class 
import unittest

from city_function import get_city_name

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = get_city_name('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does a simple city, country and population pair work?"""
        santiago_chile = get_city_name('santiago', 'chile','5000000')
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()