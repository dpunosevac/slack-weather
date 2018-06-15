import unittest

from weather import weather_handler


class TestWeather(unittest.TestCase):
    """ Tests handler methods """

    def test_weather_handler(self):
        """ Tests get_weather """
        res = weather_handler(None, None)
        self.assertEqual(400, res['statusCode'])
        self.assertEqual("Bad request. Missing 'name' in request body.", res['body'])


if __name__ == '__main__':
    unittest.main()
