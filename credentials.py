def get_credentials(filepath="secret.txt"):
    with open(filepath, 'r') as file:
        username = file.readline().strip() 
        password = file.readline().strip()  
    return username, password
