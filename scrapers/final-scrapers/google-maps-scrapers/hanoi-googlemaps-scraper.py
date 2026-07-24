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
    "&limit_per_input=134"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Hanoi+Old+Quarter/@21.034059,105.8506368,17z/data=!3m1!4b1!4m6!3m5!1s0x3135abbe12384aa7:0x595317f27fe2548e!8m2!3d21.034059!4d105.8506368!16s%2Fg%2F11b8tc18h5?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ho%C3%A0n+Ki%E1%BA%BFm+Lake/@21.0287748,105.8523647,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab953357c995:0x1babf6bb4f9a20e!8m2!3d21.0286669!4d105.8521484!16zL20vMGdwNjV3?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Train+Street/@21.0287748,105.8523647,17z/data=!4m6!3m5!1s0x3135ab3223bf135d:0xdfb7769115eddbab!8m2!3d21.0300605!4d105.8441561!16s%2Fg%2F11kqnwgtpg?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ho+Chi+Minh's+Mausoleum/@21.0368973,105.8346667,17z/data=!3m1!4b1!4m6!3m5!1s0x3135aba15ec15d17:0x620e85c2cfe14d4c!8m2!3d21.0368973!4d105.8346667!16s%2Fm%2F02xbhg7?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Temple+Of+Literature/@21.0281175,105.8356692,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab9926e7bd67:0x580e078874d5df1e!8m2!3d21.0281175!4d105.8356692!16zL20vMGI5aGp6?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/West+Lake/@21.0417888,105.7681719,11.97z/data=!4m6!3m5!1s0x3135aafe7260066b:0x4c2c988309aaa3db!8m2!3d21.053238!4d105.8260943!16s%2Fm%2F03c_2x5?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/St+Joseph+Cathedral/@21.058032,105.8238219,15z/data=!4m6!3m5!1s0x3135ab95a54c4d75:0xa3a23a6f97807c57!8m2!3d21.0286746!4d105.8488602!16s%2Fg%2F11z5nc_855?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/%C4%90%E1%BB%93ng+Xu%C3%A2n+Market,+Ph%E1%BB%91+c%E1%BB%95+H%C3%A0+N%E1%BB%99i,+Ho%C3%A0n+Ki%E1%BA%BFm,+H%C3%A0+N%E1%BB%99i+100000,+Vietnam/@21.0381434,105.8500387,17z/data=!3m1!4b1!4m6!3m5!1s0x3135abb8e6c24487:0xd9def483e7f217e6!8m2!3d21.0381434!4d105.8500387!16s%2Fm%2F09v1r31?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/The+Note+Coffee/@21.0315927,105.8508961,17z/data=!3m1!4b1!4m6!3m5!1s0x3135abbfc294b397:0xd53005101f42b4af!8m2!3d21.0315927!4d105.8508961!16s%2Fg%2F1263t5y9t?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ch%E1%BB%A3+H%C3%A0ng+M%C3%A3/@21.036447,105.8459231,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab6c6820063d:0x47e3ded8903c87f1!8m2!3d21.036442!4d105.848498!16s%2Fg%2F11h_3wvl8s?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Imperial+Citadel+of+Thang+Long/@21.0352231,105.8402594,17z/data=!3m1!4b1!4m6!3m5!1s0x3135aba3381d7c49:0xb521a7d98f582937!8m2!3d21.0352231!4d105.8402594!16s%2Fm%2F05zw9vk?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Cafe+Gi%E1%BA%A3ng/@21.0392778,105.8098493,12.62z/data=!4m6!3m5!1s0x3135abc0ee85335d:0xfca3408ac50e7363!8m2!3d21.0334664!4d105.854518!16s%2Fg%2F11bxg4n3g3?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Banh+Mi+25/@21.036113,105.848577,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab74bb3716b5:0xebfbc0d84354deb3!8m2!3d21.036113!4d105.848577!16s%2Fg%2F11tw_4rt41?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ho+Chi+Minh+Museum/@21.0356409,105.8326631,17z/data=!3m1!4b1!4m6!3m5!1s0x3135aba02e1deb6f:0x949d893f040b49d1!8m2!3d21.0356409!4d105.8326631!16s%2Fm%2F03m5z77?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/B%C3%BAn+ch%E1%BA%A3+H%C6%B0%C6%A1ng+Li%C3%AAn/@21.0181373,105.8538926,17z/data=!3m1!4b1!4m6!3m5!1s0x3135abf2a4ba685d:0x7e67963f30fa90e7!8m2!3d21.0181373!4d105.8538926!16s%2Fg%2F1hm5x9fjz?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Sky+Lotte+Observation+Deck/@21.0321022,105.8126712,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab6c92399987:0xa35f66ba8443e5b3!8m2!3d21.0321022!4d105.8126712!16s%2Fg%2F11f_1k6vfw?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 134,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)