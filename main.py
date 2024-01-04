#!/usr/bin/env python3

print('Python program started..')
import requests
from auth_manager import authenticate
from datetime import datetime
from data_parser import parse_satellite_data
from plotter import plot_data

DATA_URL_TEMPLATE = 'https://www.space-track.org/basicspacedata/query/class/gp_history/NORAD_CAT_ID/58338/orderby/TLE_LINE1%20ASC/EPOCH/{start_date}--{end_date}/format/json'

def get_date_range():
    """
    Prompts the user to input start and end dates for the data retrieval.
    Validates the input and returns the dates in 'YYYY-MM-DD' format.
    """
    ## dummy = input("Confirm, that you are logged in Spacetrack")
    date_format = "%Y-%m-%d"
    start_date = '2023-11-20' #input("Enter start date (YYYY-MM-DD): ") 
    #end_date = '2023-11-30' #input("Enter end date (YYYY-MM-DD): ")
    end_date = datetime.now().strftime('%Y-%m-%d')

    try:
        datetime.strptime(start_date, date_format)
        datetime.strptime(end_date, date_format)
    except ValueError:
        raise ValueError("Input date format is incorrect, should be YYYY-MM-DD")

    return start_date, end_date

def build_data_url(start_date, end_date):
    """
    Builds the data URL with the specified start and end dates.
    """
    url = DATA_URL_TEMPLATE.format(start_date=start_date, end_date=end_date)
    return url
    
def retrieve_data(start_date, end_date):
    """
    Retrieves data from the Space-Track API for the given date range.
    """
    cookies = authenticate()
    if cookies is not None:
        data_url = build_data_url(start_date, end_date)
        response = requests.get(data_url, cookies=cookies)
        if response.status_code == 200:
            print("Data retrieval successful")
            return response.json()
        else:
            print(f"Data retrieval failed with status code {response.status_code}")
            return None
    else:
        print("Authentication failed, cannot retrieve data")
        return None

if __name__ == "__main__":
    print('Entering main loop')
    print('Running data retrieval...')
    start_date, end_date = get_date_range()
    data = retrieve_data(start_date, end_date)
    if data:
        frame = parse_satellite_data(data)
        plot_data(frame)  # Plot the data using the new plot_data function
