import requests

url = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(url)

print(response.status_code)
print(response.json())