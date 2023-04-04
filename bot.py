import requests
import json
import time
import os
import pandas as pd
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime

def check_complaints():
    # setup
    slack_token = os.environ.get('SLACK_API_TOKEN')
    client = WebClient(token=slack_token)

    # api endpoint
    COMPLAINTS_API_ENDPOINT = "https://opendata.maryland.gov/resource/cnkn-n3pr.json"

    try:
        with open('last_checked_date.txt', 'r') as f:
            last_checked_date = f.read().strip()
    except FileNotFoundError:
        with open('last_checked_date.txt', 'w') as f:
            last_checked_date = '2023-03-30'  # default date if file doesn't exist
            f.write(last_checked_date)

    # store api response, check for new complaints
    response = requests.get(COMPLAINTS_API_ENDPOINT)
    complaints_data = json.loads(response.content)

    # save as pandas df, export as csv
    df = pd.DataFrame(complaints_data)
    df.to_csv("complaints_data.csv", index=False)

    new_complaints = []
    for complaint in complaints_data:
        complaint_date = datetime.strptime(complaint['recieved_date'], '%Y-%m-%d')
        last_checked_date_obj = datetime.strptime(last_checked_date, '%Y-%m-%d')
        if complaint_date > last_checked_date_obj:
            new_complaints.append(complaint)

    # slack message
    if new_complaints:
        message = "New complaints :herb:\n\n"
        for complaint in new_complaints:
            if 'compliant' in complaint:
                message += f"  *ID:* {complaint['compliant']}\n"
            if 'recieved_date' in complaint:
                message += f"  *Submitted to MDE:* {complaint['recieved_date']}\n"
            if 'compliant_type' in complaint:
                message += f"  *Complaint Type:* {complaint['compliant_type']}\n"
            if 'incident_date' in complaint:
                message += f"  *Incident Date:* {complaint['incident_date']}\n"
            if 'county' in complaint:
                message += f"  *County:* {complaint['county']}\n"
            if 'incident_status_desc' in complaint:
                message += f"  *Status:* {complaint['incident_status_desc']}\n"
            message += "\n"

        try:
            response = client.chat_postMessage(
                channel="slack-bots",
                text=message
            )
        except SlackApiError as e:
            print(f"Error sending message: {e}")
        else:
            print("Message sent to Slack channel")

        # update last_checked_date to the received_date of the latest complaint in new_complaints
        last_checked_date = new_complaints[-1]['recieved_date']
        with open('last_checked_date.txt', 'w') as f:
            f.write(last_checked_date)
    else:
        try:
            response = client.chat_postMessage(
                channel="slack-bots",
                text="No new complaints found :herb:"
            )
        except SlackApiError as e:
            print(f"Error sending message: {e}")
        else:
            print("Message sent to Slack channel")

check_complaints()
