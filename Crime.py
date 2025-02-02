import requests
import pandas as pd

# Correct API URL with proper query parameters
api_url = "https://api.usa.gov/crime/fbi/sapi/api/estimates/states/PA"
params = {
    "from": 2020,
    "to": 2021,
    "api_key": "XauOJf8BbvzqzczeDDYpUWiiyw64H4Gta8NFYJ3d"  # Replace with a valid key
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data["results"])
    df.to_csv("crime_data.csv", index=False)
    print("Crime data saved successfully!")
else:
    print(f"Error {response.status_code}: {response.text}")  # Print detailed error message
