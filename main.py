import requests
import os
from twilio.rest import Client

# create environment variable=  export api_key=id
API_KEY = os.environ.get("api_key")
weather_url = "https://api.openweathermap.org/data/2.5/forecast?"

account_sid = os.environ.get('account')
auth_token = os.environ.get('token')

weather_params = {
    'lat': 38.9595,
    'lon': 84.3880,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(weather_url, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)
will_rain = False

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today!",
        from="+15132243456",
        to="+15132233456",
    )
