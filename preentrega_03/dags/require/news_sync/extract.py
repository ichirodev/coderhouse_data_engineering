import requests
import json
import urllib.parse
import os

def extract(query, date, file_in):
    print(date)
    start_date = f"{date}T00:00:00.000"
    end_date = f"{date}T23:59:59.999"

    url = "https://newsapi.org/v2/everything?q=" + urllib.parse.quote(query) + "&from=" + urllib.parse.quote(start_date) + "&to=" + urllib.parse.quote(end_date) + "&sortBy=publishedAt&language=en"
    headers = {"X-Api-Key": os.getenv("NEWS_API_KEY")}
    req = requests.get(url, headers=headers)
    content = req.text
    json_content = json.loads(content)
    json_formatted_str = json.dumps(json_content, indent=2)
    f = open(file_in, "w")
    f.write(json_formatted_str)
    f.close()
    print("Extraction: Success!")
