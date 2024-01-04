# Barry_1_

Welcome to the repository for Barry_1_, an application designed to fetch and visualize orbital data for satellites using the space-track.org API.

## Overview

Barry_1_ retrieves JSON data from a dynamic URL that requires authentication. The application includes a mechanism to handle authentication, parse the retrieved data, and then generate an x-y chart representing specific orbital parameters over a given date range.

### Functionality

- Authenticates against space-track.org using credentials provided in `secret.txt`.
- Uses a default NORAD catalog ID (58338) to fetch historical satellite data for a specified date range.
- Parses JSON data to extract 'APOAPSIS' and 'PERIAPSIS' orbital parameters.
- Generates an x-y chart labeling the X-axis as 'Date' and two Y-axis data sets labeled 'APOAPSIS_km' and 'PERIAPSIS_km' (both in kilometers).

## User Stories

1. Get yourself python environment, clone this repository, create secret.txt file with space-track.org credentials in same dir as main.py, edit that file: first line = username, second is password. Run main.py with command: python main.py
2. By default, the app uses NORAD catalog ID 58338 to retrieve data.
3. User can specify custom date ranges for satellite data queries, if you un-comment 2 lines in main.py
4. The chart plotting feature visualizes 'APOAPSIS' and 'PERIAPSIS' against time.

## Technologies Used (requirements.txt)

- Python programming language
- The `Requests` library for HTTP requests
- The `Matplotlib` library for generating charts
- The `pandas` library for data manipulation

## Files in the Repository

- `auth_manager.py`: Manages the authentication process with space-track.org.
- `credentials.py`: Retrieves user credentials from `secret.txt`.
- must create yourself: `secret.txt`: Contains user credentials for authentication (Please replace with your own credentials).
- `data_parser.py`: Parses the JSON data and prepares it for chart plotting.
- `main.py`: Main app for ploting and geting data from the space-track API.

## Getting Started

Before running the application, ensure you have Python and all required libraries installed. Then, create the contents of `secret.txt` with your own space-track.org credentials.

To run the application:

1. Execute `auth_manager.py` to make sure authentication works.
2. Run `python main.py` to fetch and display the satellite data.


## Contributing

Contributions to Barry_1_ are welcome. Please fork the repository and submit pull requests with your features or fixes. Ensure that your code adheres to the project's coding standards and includes appropriate tests and documentation.

## License

This project not licenced.
