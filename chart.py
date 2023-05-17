import requests
import json
import time
import os
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime

def top10chart():

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

    # complaints by county
    complaints = pd.read_csv('complaints_data.csv')
    complaints_by_county = complaints.groupby(['county']).size().reset_index(name='count')

    # top 10
    top_10_counties = complaints_by_county.nlargest(10, 'count')

    # create a horizontal bar chart
    fig = go.Figure(go.Bar(
        x=top_10_counties['count'],
        y=top_10_counties['county'],
        orientation='h',
        text=top_10_counties['count'],
        textposition='auto',
        marker=dict(color='#87ae73')
    ))

    # set chart title and axis labels
    fig.update_layout(
        title='Top 10 Maryland Counties with the Most Environmental Complaints',
        xaxis_title='Number of Complaints',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='black')
        )
    
    fig.add_annotation(
        text='Source: Maryland Department of the Environment',
        font=dict(
            family='Arial',
            size=12,
            color='#5A5A5A'
        ),
        showarrow=False,
        xref='paper',
        yref='paper',
        x=0,
        y=-.22,
        xanchor='left',
        yanchor='bottom'
    )

    # save chart as png
    try:
        fig.write_image("top_10_counties.png")
        print("Image saved successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

top10chart()
