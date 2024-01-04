import pandas as pd

def parse_satellite_data(json_data):
    """
    Parses the JSON satellite data to extract 'APOAPSIS' and 'PERIAPSIS' along with the dates.

    Parameters:
    json_data (list): A list of dictionaries, each containing satellite data.

    Returns:
    pandas.DataFrame: A dataframe with columns date, apoapsis and periapsis.
    """

    # Initialize the lists for storing extracted data
    dates = []
    apoapsises = []
    periapsises = []

    # Loop through each entry in the json data and extract relevant information
    i = 0
    for entry in json_data:
        i = i+1
        date = entry.get('EPOCH')
        apoapsis = entry.get('APOAPSIS')
        periapsis = entry.get('PERIAPSIS')

        # Append the extracted values to their respective lists
        dates.append(date)
        apoapsises.append(apoapsis)
        periapsises.append(periapsis)
        ## debug: print('Reading data frame ',i,' date is ',date,' apo=',apoapsis,' per=',periapsis)

    # Create a pandas dataframe from the lists
    data = {
        'Date': pd.to_datetime(dates),
        'APOAPSIS_km': apoapsises,
        'PERIAPSIS_km': periapsises
    }
    dataframe = pd.DataFrame(data)
    
    return dataframe
