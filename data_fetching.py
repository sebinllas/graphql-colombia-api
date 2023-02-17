import json
import requests


def get_departments():
    res = requests.get("https://api-colombia.com/api/v1/Department")
    return json.loads(res.text)
