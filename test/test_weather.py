import unittest
import getweather

#run these tests with pipenv run python -m unittest

class TestWeatherKnownName(unittest.TestCase):
  def setUp(self):
    self.result1 = getweather.printweather('Kiev')
    self.result2 = getweather.printweather('sdfsdfsdf')

  def test_should_return_description_string_for_Kiev(self):
    self.assertNotEqual(self.result1, "Something went wrong. Invalid location?")

  def test_should_return_invalid_message_with_nonsense_city_name(self):
    self.assertEqual(self.result2, "Something went wrong. Invalid location?")
