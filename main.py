#!/usr/bin/env python3

print('Python program started..')
import requests
from auth_manager import authenticate
from datetime import datetime
from data_parser import parse_satellite_data
from plotter import plot_data
start_date_str = '2023-11-20' #input("Enter start date (YYYY-MM-DD): ") 
end_date_str = datetime.now().strftime('%Y-%m-%d')
DATA_URL_TEMPLATE = 'https://www.space-track.org/basicspacedata/query/class/gp_history/NORAD_CAT_ID/58338/orderby/TLE_LINE1%20ASC/EPOCH/{start_date}--{end_date}/format/json'

def get_date_range():
    """
    Prompts the user to input start and end dates for the data retrieval.
    Validates the input and returns the dates in 'YYYY-MM-DD' format.
    """
    ## dummy = input("Confirm, that you are logged in Spacetrack")
    date_format = "%Y-%m-%d"
    start_date_str = '2023-11-20' #input("Enter start date (YYYY-MM-DD): ") 
    #end_date_str = '2023-11-30' #input("Enter end date (YYYY-MM-DD): ")
    end_date_str = datetime.now().strftime('%Y-%m-%d')

    try:
        datetime.strptime(start_date_str, date_format)
        datetime.strptime(end_date_str, date_format)
    except ValueError:
        raise ValueError("Input date format is incorrect, should be YYYY-MM-DD")

    return start_date_str, end_date_str

def build_data_url(start_date_str, end_date_str):
    """
    Builds the data URL with the specified start and end dates.
    """
    url = DATA_URL_TEMPLATE.format(start_date=start_date_str, end_date=end_date_str)
    return url
    
def retrieve_data(start_date_str, end_date_str):
    """
    Retrieves data from the Space-Track API for the given date range.
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    if start_date >= end_date:
        raise ValueError("Start date must be before end date")
    
    cookies = authenticate()
    if cookies is not None:
        data_url = build_data_url(start_date_str, end_date_str)
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
