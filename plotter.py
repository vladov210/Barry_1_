import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Determine an appropriate locator interval based on the date range
def determine_locator_interval(dates_series):
    date_range = (dates_series.max() - dates_series.min()).days
    if date_range <= 30:
        return 1  # Daily ticks
    elif date_range <= 180:
        return 7  # Weekly ticks
    else:
        return 30  # Monthly ticks

def plot_data(df):
    # Convert 'Date' from string to datetime if necessary
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        df['Date'] = pd.to_datetime(df['Date'])
        print('Some dates converted..')
    # Sort the dataframe by 'Date' before plotting
    df.sort_values(by='Date', inplace=True)

    locator_interval = determine_locator_interval(df['Date'])

    # Setting the Date format and locator interval for better readability
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=locator_interval))

    # Convert APOAPSIS and PERIAPSIS columns to float
    df['APOAPSIS_km'] = df['APOAPSIS_km'].astype(float)
    df['PERIAPSIS_km'] = df['PERIAPSIS_km'].astype(float)
    
    # Filter out any rows with negative or non-numeric APOAPSIS or PERIAPSIS values
    df = df[(df['APOAPSIS_km'] > 0) & (df['PERIAPSIS_km'] > 0) ]
    
    # Set the plot size for better visibility
    plt.close('all')
    fig=plt.figure(figsize=(10, 5))
    
    # Plot APOAPSIS values
    plt.plot(df['Date'], df['APOAPSIS_km'], label='APOAPSIS (km)', marker='o')

    # Plot PERIAPSIS values
    plt.plot(df['Date'], df['PERIAPSIS_km'], label='PERIAPSIS (km)', marker='x')

    # Labeling the x-axis and y-axis
    plt.xlabel('Date')
    plt.ylabel('km')

    plt.title('APOAPSIS and PERIAPSIS over Time')

    plt.xticks(rotation=45)

    plt.legend()

    plt.ylim(ymin=min(df['PERIAPSIS_km']))
    plt.tight_layout()
    plt.show()
    