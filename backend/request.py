import requests
import time

API_KEY = "HTMP1ih07mZXw8foEXC8Py5z7gCi-N_UWiz8RzwVKavyUTJyAXxzGu-n1tr2-0-6lojpBZRUI1rOg59NFpYezQ"
BASE_URL = "https://api.musicgpt.com/api/public/v1/MusicAI"

task_id = "1094cdad-7c6b-4d75-b02d-efa3526adc26"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Try different endpoint patterns
endpoints_to_try = [
    f"{BASE_URL}/status/{task_id}",
    f"{BASE_URL}/task/{task_id}",
    f"{BASE_URL}/job/{task_id}",
    f"{BASE_URL}/{task_id}",
    f"{BASE_URL}?task_id={task_id}",
]

print("Testing different endpoint patterns...\n")

for endpoint in endpoints_to_try:
    print(f"Trying: {endpoint}")
    response = requests.get(endpoint, headers=headers)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text[:200]}\n")
    
    if response.status_code == 200:
        print("✓ Found working endpoint!")
        data = response.json()
        print(f"Full response: {data}")
        break
else:
    print("\n--- None of the standard patterns worked ---")
    print("Please check the MusicGPT API documentation for the correct status endpoint")
    print("\nAlternatively, try GET request to base URL:")
    
    response = requests.get(BASE_URL, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")