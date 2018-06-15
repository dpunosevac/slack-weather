import logging
import os
import re
import json

from botocore.vendored import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def weather_handler(event, context):
    if context is not None:
        logger.info("Received request with id '{}'".format(
            context.aws_request_id))

    if event is not None:
        str_obj = json.loads(json.dumps(event["body"]))
        m = re.search('&text=(.+?)&', str_obj)

        if m:
            params = {
                "q": m.group(1),
                "appid": os.environ.get("API_KEY")
            }

            response = requests.get(BASE_URL, params=params)

            json_obj = json.loads(response.text)
            
            weather = json_obj["weather"][0]["description"].title()
            temp = json_obj["main"]["temp"] - 273.15
            pressure = json_obj["main"]["pressure"]
            humidity = json_obj["main"]["humidity"]
            temp_min = json_obj["main"]["temp_min"] - 273.15
            temp_max = json_obj["main"]["temp_max"] - 273.15
            ws = json_obj["wind"]["speed"]
            ws_description = ""

            if ws < 0.3:
                ws_description = "Calm"
            elif ws < 1.5:
                ws_description = "Light air"
            elif ws < 3.3:
                ws_description = "Light breeze"
            elif ws < 5.5:
                ws_description = "Gentle breeze"
            elif ws < 8.0:
                ws_description = "Moderate breeze"
            elif ws < 11.0:
                ws_description = "Fresh breeze"
            elif ws < 14.0:
                ws_description = "Strong breeze"
            elif ws < 17.0:
                ws_description = "High wind"
            elif ws < 20.0:
                ws_description = "Gale"
            elif ws < 24.0:
                ws_description = "Strong gale"
            elif ws < 28.0:
                ws_description = "Storm"
            elif ws < 32.0:
                ws_description = "Violent storm"
            elif ws >= 33.0:
                ws_description = "Hurricane"
            else:
                ws_description = "Calm"

            wd = json_obj["wind"]["deg"]
            wd_description = ""

            if 348.75 > wd <= 11.25:
                wd_description = "North"
            elif 11.25 > wd <= 33.75:
                wd_description = "North-northeast"
            elif 33.75 > wd <= 56.25:
                wd_description = "Northeast"
            elif 56.25 > wd <= 78.75:
                wd_description = "East-northeast"
            elif 78.75 > wd <= 101.25:
                wd_description = "East"
            elif 101.25 > wd <= 123.75:
                wd_description = "East-southeast"
            elif 123.75 > wd <= 146.25:
                wd_description = "Southeast"
            elif 146.25 > wd <= 168.75:
                wd_description = "South-southeast"
            elif 168.75 > wd <= 191.25:
                wd_description = "South"
            elif 191.25 > wd <= 213.75:
                wd_description = "South-southwest"
            elif 213.75 > wd <= 236.25:
                wd_description = "Southwest"
            elif 236.25 > wd <= 258.75:
                wd_description = "West-southwest"
            elif 258.75 > wd <= 281.25:
                wd_description = "West"
            elif 281.25 > wd <= 303.75:
                wd_description = "West-northwest"
            elif 303.75 > wd <= 326.25:
                wd_description = "Northwest"
            elif 326.25 > wd <= 348.75:
                wd_description = "North-northwest"
            else:
                wd_description = ""

            city = json_obj["name"]

            response_msg = "{} in {}. Current temperature is {}. Pressure is {} hpa. Humidity is {}%. Minimal temperature is {} and maximum is {}.".format(weather, city, temp, pressure, humidity, temp_min, temp_max)

            return {
                "statusCode": response.status_code,
                "body": response_msg,
            }

    return {
        "statusCode": 400,
        "body": "Bad request. Check if your head has 'Content-Type: application/x-www-form-urlencoded' and 'text' property.",
    }
