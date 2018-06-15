import unittest

from weather import weather_handler


class TestWeather(unittest.TestCase):
    """ Tests handler methods """

    def test_weather_handler(self):
        """ Tests get_weather """
        res = weather_handler(None, None)
        self.assertEqual(400, res['statusCode'])
        self.assertEqual("Bad request. Check if your head has 'Content-Type: application/x-www-form-urlencoded' and 'text' property.", res['body'])


if __name__ == '__main__':
    unittest.main()
