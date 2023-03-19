import requests
import json
import time
import os 
from slack import WebClient
from slack.errors import SlackApiError

# setup
slack_token = os.environ.get(‘SLACK_API_TOKEN’)
client = WebClient(token=slack_token)

# api endpoint
COMPLAINTS_API_ENDPOINT = "https://opendata.maryland.gov/resource/cnkn-n3pr.json"

last_update = 0

while True:
    # get request
    response = requests.get(COMPLAINTS_API_ENDPOINT)
    complaints_data = json.loads(response.content)

    # check for new complaints since last update
    new_complaints = []
    for complaint in complaints_data:
        if complaint['recieved_date'] > last_update:
            new_complaints.append(complaint)

    # message formatting 
    if new_complaints:
        message = f"New complaints:\n"
        for complaint in new_complaints:
            message += f"- A complaint for {complaint['compliant_type']} was submitted on ({complaint['recieved_date']})\n"
            message += f"  ID: {complaint['compliant']}\n"
            message += f"  Incident date: {complaint['incident_date']}\n"
            message += f"  County: {complaint['county']}\n"
            message += f"  Status: {complaint['incident_status_desc']}\n"

        try:
            response = client.chat_postMessage(
                channel= "slack-bots",
                text=message
            )
        except SlackApiError as e:
            print(f"Error sending message: {e}")
        else:
            print("Message sent to Slack channel")

    # update last update time
    last_update_time = complaints_data[-1]['wait

    # wait for 1 day before checking again
    time.sleep(1440)
