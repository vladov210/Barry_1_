import requests
from credentials import get_credentials

SPACE_TRACK_LOGIN_URL = 'https://www.space-track.org/ajaxauth/login' ## Check that this URL is correctly set

def authenticate():
    username, password = get_credentials()
    ##print(f'Read credentials: username={username}, password={password}')  # Debug: Print the credentials to confirm they are read correctly
    payload = {
        'identity': username,
        'password': password
    }
    response = requests.post(SPACE_TRACK_LOGIN_URL, data=payload)
    
    if response.status_code == 200:
        print("Authentication successful")
        return response.cookies
    else:
        print(f"Authentication failed with status: {response.status_code}")
        return None

if __name__ == "__main__":
    authenticate()
