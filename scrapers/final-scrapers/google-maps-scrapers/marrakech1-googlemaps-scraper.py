from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_TOKEN = os.getenv("BRIGHTDATA_API_TOKEN")

if API_TOKEN is None:
    raise ValueError("BRIGHTDATA_API_TOKEN not found")

url = (
    "https://api.brightdata.com/datasets/v3/scrape"
    "?dataset_id=gd_luzfs1dn2oa0teb81"
    "&notify=true"
    "&include_errors=true"
    "&limit_per_input=119"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Agafay+Desert/@31.4896832,-8.492845,11z/data=!4m7!3m6!1s0xdafdf6935e5e5c3:0x34513cc3fb2fc34e!8m2!3d31.4882226!4d-8.1942373!15sCg1BZ2FmYXkgZGVzZXJ0Wg8iDWFnYWZheSBkZXNlcnSSARJ0b3VyaXN0X2F0dHJhY3Rpb26aAURDaTlEUVVsUlFVTnZaRU5vZEhsalJqbHZUMnRHYTFNeGJGSldhMlJwVGtoc2QyRlhXVFZsUjA1VVVXdGFabUpZWXhBQuABAPoBBAgfED0!16s%2Fg%2F11t5d2n2ms?entry=tts&g_ep=EgoyMDI2MDcyMS4wIPu8ASoASAFQAw%3D%3D&skid=dccac5fc-de9c-4623-865b-8be01153abde",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 119,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)