
import requests
import json
# Fetching data from the World Bank API

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20]


def process_data():
  for year in last_twenty_years:
      if not year["value"]:
          continue
      
      display_width = year["value"] // 10_000_000
      print(display_width * "=")
      
process_data()