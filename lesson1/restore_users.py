import requests
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
output_file = base_dir / "user_from_api.json"

print("SAVING TO:", output_file)

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    data = response.json()
    print("NUMBER OF USERS FROM API:", len(data))

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("RESTORED SUCCESSFULLY")
else:
    print("FAILED TO FETCH USERS:", response.status_code)
