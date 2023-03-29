import requests
import json
import time
import os
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime

# setup
slack_token = os.environ.get('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

# api endpoint
COMPLAINTS_API_ENDPOINT = "https://opendata.maryland.gov/resource/cnkn-n3pr.json"

response = requests.get(COMPLAINTS_API_ENDPOINT)
complaints_data = json.loads(response.content)
last_update = complaints_data[-1]['recieved_date']

while True:
    # get request
    response = requests.get(COMPLAINTS_API_ENDPOINT)
    complaints_data = json.loads(response.content)

    # check for new complaints since last update
    new_complaints = []
    for complaint in complaints_data:
        complaint_datetime = datetime.strptime(
            complaint['recieved_date'], "%Y-%m-%d")
        last_update_datetime = datetime.strptime(last_update, "%Y-%m-%d")
        if complaint_datetime > last_update_datetime:
            new_complaints.append(complaint)

    # slack message
    if new_complaints:
        message = f"New complaints:\n"
        for complaint in new_complaints:
            if 'complaint_type' and 'recieved_date' in new_complaints:
                message += f"- A complaint for {complaint['compliant_type']} was submitted on ({complaint['recieved_date']})\n"
            if 'compliant' in new_complaints:
                message += f"  ID: {complaint['compliant']}\n"
            if 'incident_date' in new_complaints:
                message += f"  Incident date: {complaint['incident_date']}\n"
            if 'county' in new_complaints:
                message += f"  County: {complaint['county']}\n"
            if 'incident_status_desc' in new_complaints:
                message += f"  Status: {complaint['incident_status_desc']}\n"

        try:
            response = client.chat_postMessage(
                channel="slack-bots",
                text=message
            )
        except SlackApiError as e:
            print(f"Error sending message: {e}")
        else:
            print("Message sent to Slack channel")

    # update last update time
    last_update = new_complaints[-1]['recieved_date']