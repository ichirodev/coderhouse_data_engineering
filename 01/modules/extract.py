import requests
import json
import urllib.parse
import os

def extract(query, start_date, end_date, file_in):
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
