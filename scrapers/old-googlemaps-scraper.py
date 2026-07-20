from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_TOKEN = os.getenv("BRIGHTDATA_API_TOKEN")

if API_TOKEN is None:
    raise ValueError("BRIGHTDATA_API_TOKEN not found")

url = (
    "https://api.brightdata.com/datasets/v3/scrape"
    "?dataset_id=gd_luzfs1dn2oa0teb81"
    "&notify=false"
    "&include_errors=true"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

places = [
    # castelo de sao jorge
    "https://www.google.com/maps/place/Castelo+de+S%C3%A3o+Jorge/@38.7139092,-9.171585,14z/data=!4m7!3m6!1s0xd193477b40ec39b:0xb4c0704199e433d7!8m2!3d38.7139092!4d-9.1334762!15sChpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc1ocIhpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc5IBBmNhc3RsZZoBRENpOURRVWxSUVVOdlpFTm9kSGxqUmpsdlQydG9XR0pGUmtSTmEyUTJUbFpWZWs1V1RrMVZhbHBLWW1wck1WUnVZeEFC4AEA-gEECAAQPg!16zL20vMDgybDJw?entry=tts&g_ep=EgoyMDI2MDcwNy4wIPu8ASoASAFQAw%3D%3D&skid=595716b7-f5f0-4a8e-90f1-d6cdafacc364" 
]

payload = {
    "input": [
        {
            "url": place,
            # "days_limit": 30,   #MAYBE CHANGE THIS
            "sort_by": "Newest",
        }
        for place in places
    ],
    "limit_per_input": 5    #CHANGE THIS
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)