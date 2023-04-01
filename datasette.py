import requests
import json
import pandas as pd

# api endpoint
COMPLAINTS_API_ENDPOINT = "https://opendata.maryland.gov/resource/cnkn-n3pr.json"

# store api response
response = requests.get(COMPLAINTS_API_ENDPOINT)
complaints_data = json.loads(response.content)

# convert json data to df
df = pd.DataFrame(complaints_data)

# save as csv
df.to_csv("complaints_data.csv", index=False)