import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Error: Received HTTP status code {response.status_code}")
            return None

        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected JSON format")
            return None

        for user in users[:num_users]:
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")

            print("Name:", name)
            print("Email:", email)
            print("City:", city)
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)
        return None


fetch_and_display_users(4)
fetch_and_display_users(16)