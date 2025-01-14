from requests import get  # pip install requests
import requests

# Info cPanel
cpanel_url = "xxxx"  # URL cPanel
cpanel_user = "xxx"           # Account cPanel
cpanel_token = "xxxx"                # Token API cPanel

# Account to delete
email = "xxxx"                      
domain = "Example.com"                  

# API Endpoint and headers
endpoint = f"{cpanel_url}/execute/Email/delete_pop"
headers = {
    "Authorization": f"cpanel {cpanel_user}:{cpanel_token}",
}

# Payload
payload = {
    "email": email,
    "domain": domain,
}

response = requests.post(endpoint, headers=headers, data=payload)

if response.status_code == 200:
    result = response.json()
    if result.get("status") == 1:  
        print("Email user deleted successfully!")
    else: 
        print(f"Failed to delete email: {result.get('errors')}")
else:
    print(f"HTTP Error: {response.status_code}")
    print("Response:", response.text)
