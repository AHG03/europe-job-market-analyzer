import requests

url = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(url)
data = response.json()
jobs = data["data"]


for job in jobs[:5]:
    print(f"""
Title: {job["title"]}
Company: {job["company_name"]}
Location: {job["location"]}
Tags: {", ".join(job["tags"])}
""")