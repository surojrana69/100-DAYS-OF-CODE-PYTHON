import os
import requests
from twilio.rest import Client

website_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("AC_SID")
auth_token = os.environ.get("AUTH_TOKEN_KEY")

parameters = {
    "lat": 47.54,
    "lon": 14.88,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=website_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring your umbrella ☔",
        from_="twilio number",
        to="receiver",
    )
    print(f"Message sent! Status: {message.status}")
else:

    print("No rain forecast for these coordinates. No SMS sent.")