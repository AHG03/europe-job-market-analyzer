import requests
import json
from pathlib import Path

API_URL = "https://www.arbeitnow.com/api/job-board-api"

def fetch_jobs():
    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception("API request failed")

    return response.json()

def save_jobs(data):
    output_path = Path("../../data/raw/jobs_raw.json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:
        json.dump(data, file, indent = 2)

    print(f"Saved jobs to {output_path}")

def main():
    data = fetch_jobs()
    save_jobs(data)

if __name__ == "__main__":
    main()