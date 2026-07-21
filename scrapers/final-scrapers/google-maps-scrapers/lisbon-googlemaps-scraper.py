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
    "&limit_per_input=1"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        # sample
        {
            "url":"",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # castelo de sao jorge
        {
            "url":"https://www.google.com/maps/place/Castelo+de+S%C3%A3o+Jorge/@38.7139092,-9.171585,14z/data=!4m6!3m5!1s0xd193477b40ec39b:0xb4c0704199e433d7!8m2!3d38.7139092!4d-9.1334762!16zL20vMDgybDJw?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # jeronimos monastery
        {
            "url":"https://www.google.com/maps/place/Jer%C3%B3nimos+Monastery/@38.6978909,-9.2448127,14z/data=!4m6!3m5!1s0xd1ecb42c3c29c4b:0x87755d348e96ebed!8m2!3d38.6978909!4d-9.2067039!16zL20vMDUwOWt2?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # carmo archaelogical museum
        {
            "url":"https://www.google.com/maps/place/Carmo+Archaeological+Museum/@38.7120383,-9.1787217,14z/data=!3m1!5s0xd19347f4bd8b7d7:0xd780cc121205771!4m6!3m5!1s0xd19347f372ec63f:0x32d7f56592e02cef!8m2!3d38.7120383!4d-9.1406129!16zL20vMGdxNG41?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # praca do comercio
        {
            "url":"https://www.google.com/maps/place/Pra%C3%A7a+do+Com%C3%A9rcio/@38.7120383,-9.1787217,14z/data=!4m6!3m5!1s0xd19347a30a54b63:0x30532f5f6b28e044!8m2!3d38.7072828!4d-9.1363613!16zL20vMGczbDNz?entry=ttu&g_ep=EgoyMDI2MDcxNS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # miradouro de santa luzia
        {
            "url":"https://www.google.com/maps/place/Miradouro+de+Santa+Luzia/@38.7120383,-9.1787217,14z/data=!4m7!3m6!1s0xd1933849770e4c7:0x41203b21edcd2769!8m2!3d38.7116956!4d-9.1301972!15sChpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc1ocIhpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc5IBC3NjZW5pY19zcG90mgEjQ2haRFNVaE5NRzluUzBWSlEwRm5UVU5aY1dGdVdrSjNFQUXgAQD6AQQIMxBL!16s%2Fg%2F1216ftv9?entry=tts&g_ep=EgoyMDI2MDcwNy4wIPu8ASoASAFQAw%3D%3D&skid=31172975-ab78-48b3-8d6d-c4cb9341f16f",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # palacio nacional da ajuda
        {
            "url":"https://www.google.com/maps/place/Pal%C3%A1cio+Nacional+da+Ajuda/@38.7076247,-9.2360865,14z/data=!4m7!3m6!1s0xd1ecb5671734dcb:0x6d73ed20fdd5778b!8m2!3d38.7076247!4d-9.1979777!15sChpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc1ocIhpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc5IBF2hpc3RvcmljYWxfcGxhY2VfbXVzZXVtmgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJTY2psaE9HNW5SUkFC4AEA-gEFCKYGEEE!16zL20vMDkzN2g2?entry=tts&g_ep=EgoyMDI2MDcwNy4wIPu8ASoASAFQAw%3D%3D&skid=25e6d1ad-84f0-42af-a7d7-36b595fe94c5",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
        # history of lisbon mural
        {
            "url":"https://www.google.com/maps/place/History+of+Lisbon+Mural+by+Nuno+Saraiva/@38.7076247,-9.2360865,14z/data=!4m7!3m6!1s0xd1935b56d72054f:0x4cf3d5b1c11704ed!8m2!3d38.7120179!4d-9.1301211!15sChpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc1ocIhpsaXNib24gdG91cmlzdCBhdHRyYWN0aW9uc5IBEnRvdXJpc3RfYXR0cmFjdGlvbpoBJENoZERTVWhOTUc5blMwVkpRMEZuU1VOMWEyVlVlakJSUlJBQuABAPoBBAgAEEQ!16s%2Fg%2F11h5_sp0hs?entry=tts&g_ep=EgoyMDI2MDcwNy4wIPu8ASoASAFQAw%3D%3D&skid=04152800-d18a-4a92-857f-880321348e67",
            "days_limit":182,
            "sort_by":"Most relevant"
        },
    ],  
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