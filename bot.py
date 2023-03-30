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

# store initial api response, set last_update
response = requests.get(COMPLAINTS_API_ENDPOINT)
complaints_data = json.loads(response.content)
last_update = complaints_data[-1]['recieved_date']

while True:
    # check for new complaints
    response = requests.get(COMPLAINTS_API_ENDPOINT)
    complaints_data = json.loads(response.content)

    new_complaints = []
    for complaint in complaints_data:
        complaint_datetime = datetime.strptime(
            complaint['recieved_date'], "%Y-%m-%d")
        last_update_datetime = datetime.strptime(last_update, "%Y-%m-%d")
        if complaint_datetime > last_update_datetime:
            new_complaints.append(complaint)

    # slack message
    if new_complaints:
        message = "New complaints:\n"
        for complaint in new_complaints:
            if 'complaint_type' in complaint and 'recieved_date' in complaint:
                message += f"- A complaint for {complaint['complaint_type']} was submitted on ({complaint['recieved_date']})\n"
            if 'compliant' in complaint:
                message += f"  ID: {complaint['compliant']}\n"
            if 'incident_date' in complaint:
                message += f"  Incident date: {complaint['incident_date']}\n"
            if 'county' in complaint:
                message += f"  County: {complaint['county']}\n"
            if 'incident_status_desc' in complaint:
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

        # update last_update to the received_date of the latest complaint in new_complaints
        last_update = new_complaints[-1]['recieved_date']
