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
    "&notify=false"
    "&include_errors=true"
    "&limit_per_input=1"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        # castelo de sao jorge
        {
            "url":"https://www.google.com/maps/place/Castelo+de+S%C3%A3o+Jorge/@38.7139092,-9.171585,14z/data=!4m6!3m5!1s0xd193477b40ec39b:0xb4c0704199e433d7!8m2!3d38.7139092!4d-9.1334762!16zL20vMDgybDJw?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Newest"
        },
        # carmo archaeological museum
        {
            "url":"https://www.google.com/maps/place/Carmo+Archaeological+Museum/@38.7120383,-9.1787217,14z/data=!3m1!5s0xd19347f4bd8b7d7:0xd780cc121205771!4m6!3m5!1s0xd19347f372ec63f:0x32d7f56592e02cef!8m2!3d38.7120383!4d-9.1406129!16zL20vMGdxNG41?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Newest"
        }],
    "limit_per_input": 1,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)