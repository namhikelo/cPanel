from requests import get  # pip install requests
import requests

# Infomation cPanel
cpanel_url = "https://x.x.x.x:2083"  # URL cPanel
cpanel_user = "xxx"           # Account cPanel
cpanel_token = "xxxx"                # Token API cPanel

# Create Account
email = "xxx"                       
domain = "example.com"                      
password = "StrongPassword123!"                
quota = 100                                    

# API Endpoint và headers
endpoint = f"{cpanel_url}/execute/Email/add_pop"
headers = {
    "Authorization": f"cpanel {cpanel_user}:{cpanel_token}",
}

# Payload
payload = {
    "email": email,
    "domain": domain,
    "password": password,
    "quota": quota,
}

response = requests.post(endpoint, headers=headers, data=payload)

if response.status_code == 200:
    result = response.json()
    if result.get("status") == 1:  # Thành công
        print("Email created successfully!")
    else:  # Thất bại
        print(f"Failed to create email: {result.get('errors')}")
else:
    print(f"HTTP Error: {response.status_code}")
    print("Response:", response.text)
