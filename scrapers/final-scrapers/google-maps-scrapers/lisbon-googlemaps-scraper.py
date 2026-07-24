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
    "&limit_per_input=86"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Alfama,+Lisbon,+Portugal/@38.7117719,-9.1316655,17z/data=!3m1!4b1!4m6!3m5!1s0xd19347613ee43b5:0xc37964f5e5b83e8!8m2!3d38.7124976!4d-9.1303235!16s%2Fg%2F11bc5gtvcs?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bel%C3%A9m+Tower/@38.6915837,-9.2159773,17z/data=!3m2!4b1!5s0xd1ecb6968ca6973:0x7ffc53d5b48b9149!4m6!3m5!1s0xd1ecb42c3c29c4b:0x3002dcadcf52513f!8m2!3d38.6915837!4d-9.2159773!16zL20vMDVnYng2?entry=tts&g_ep=EgoyMDI2MDcxOS4wIPu8ASoASAFQAw%3D%3D&skid=7d487d55-b3a0-4149-a1a4-ef2f314168c1",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bairro+Alto,+Margueira,+Lisbon,+Portugal/@38.7134511,-9.1453838,17z/data=!3m1!4b1!4m6!3m5!1s0xd19348002b3abfb:0xbafe2a3ba260d0f1!8m2!3d38.7128331!4d-9.1450582!16zL20vMDU1NHR6?entry=tts&g_ep=EgoyMDI2MDcxOS4wIPu8ASoASAFQAw%3D%3D&skid=b3ae1755-b195-4f3e-a35c-38f79355a13d",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Cascais,+Portugal/@38.6748551,-9.2526578,11.46z/data=!4m6!3m5!1s0xd1ec47379b79a97:0x870d3b7e1807bbc2!8m2!3d38.6960614!4d-9.4303646!16s%2Fm%2F080gb24?entry=tts&g_ep=EgoyMDI2MDcxOS4wIPu8ASoASAFQAw%3D%3D&skid=fee6503d-5938-4000-a2f0-533d6a4e8ed0",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Chiado,+1200-443+Lisbon,+Portugal/@38.7105417,-9.1422039,15z/data=!3m1!4b1!4m6!3m5!1s0xd19347f02a6390f:0xe0051c566fdc1e97!8m2!3d38.7105423!4d-9.1422039!16s%2Fm%2F02vy_rs?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/LX+Factory/@38.7034602,-9.1787831,17z/data=!3m1!4b1!4m6!3m5!1s0xd1934af61dedbe5:0x33ebaaaa14f543ac!8m2!3d38.7034602!4d-9.1787831!16s%2Fg%2F1q63cnck4?entry=tts&g_ep=EgoyMDI2MDcxOS4wIPu8ASoASAFQAw%3D%3D&skid=dd5aa7f6-a9ff-4b04-9157-489c18be76ba",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Jer%C3%B3nimos+Monastery/@38.6978909,-9.2067039,17z/data=!3m1!4b1!4m6!3m5!1s0xd1ecb42c3c29c4b:0x87755d348e96ebed!8m2!3d38.6978909!4d-9.2067039!16zL20vMDUwOWt2?entry=tts&g_ep=EgoyMDI2MDcxOS4wIPu8ASoASAFQAw%3D%3D&skid=e1a1a33e-0ef8-4b53-9823-e3d56b338997",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Time+Out+Market/@38.7070608,-9.1456691,17z/data=!3m2!4b1!5s0xd193487578f2575:0x98e82030e12dfce0!4m6!3m5!1s0xd193487595e6075:0x138fe14e4972dc92!8m2!3d38.7070608!4d-9.1456691!16s%2Fg%2F11c2pm29hf?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Past%C3%A9is+de+Bel%C3%A9m/@38.6975105,-9.2032276,17z/data=!3m2!4b1!5s0xd1ecb452eeecc51:0xfe3cb68ec8239ac7!4m6!3m5!1s0xd1ecb452efd715b:0xffeff6c6b46d9665!8m2!3d38.6975105!4d-9.2032276!16s%2Fg%2F1q5bm9555?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Pra%C3%A7a+do+Com%C3%A9rcio/@38.7072828,-9.1363613,17z/data=!3m1!4b1!4m6!3m5!1s0xd19347a30a54b63:0x30532f5f6b28e044!8m2!3d38.7072828!4d-9.1363613!16zL20vMGczbDNz?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Pink+Street/@38.7072464,-9.1437847,17z/data=!3m1!4b1!4m6!3m5!1s0xd19352efae3f381:0x98d83ac3037bab1e!8m2!3d38.7072464!4d-9.1437847!16s%2Fg%2F11kbz8xq67?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/National+Palace+of+Pena/@38.7875851,-9.3906089,17z/data=!3m1!4b1!4m6!3m5!1s0xd1edabff29c5a67:0x77271a7dcb673b58!8m2!3d38.7875851!4d-9.3906089!16zL20vMDI5OGYx?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Miradouro+da+Senhora+do+Monte/@38.7192091,-9.1327772,17z/data=!3m1!4b1!4m6!3m5!1s0xd19338f34837d57:0x611f8deb59a26af4!8m2!3d38.7192091!4d-9.1327772!16s%2Fg%2F120zpds0?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Santa+Justa+Lift/@38.7121023,-9.1394375,17z/data=!3m1!4b1!4m6!3m5!1s0xd193478b78a8d2f:0xe1147c62e070697c!8m2!3d38.7121301!4d-9.1394297!16zL20vMDYydGw1?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/MAAT+-+Museum+of+Art,+Architecture+and+Technology/@38.6958561,-9.193312,17z/data=!3m1!4b1!4m6!3m5!1s0xd1ecb4dd3e5f491:0xcb13504c19595bc4!8m2!3d38.6958561!4d-9.193312!16s%2Fg%2F11cs3vkn8z?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Miradouro+de+S%C3%A3o+Pedro+de+Alc%C3%A2ntara/@38.7255038,-9.1740754,13.34z/data=!4m6!3m5!1s0xd19338037000861:0x1beb7972336de3a1!8m2!3d38.7153095!4d-9.1441762!16s%2Fg%2F1224hf85?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Castelo+de+S%C3%A3o+Jorge/@38.7139092,-9.1334762,17z/data=!3m1!4b1!4m6!3m5!1s0xd193477b40ec39b:0xb4c0704199e433d7!8m2!3d38.7139092!4d-9.1334762!16zL20vMDgybDJw?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Miradouro+de+Santa+Catarina,+1200-012+Lisboa,+Portugal/@38.7095753,-9.1476555,17z/data=!3m1!4b1!4m6!3m5!1s0xd193480f06596a3:0x96e9334cb717ce28!8m2!3d38.7095364!4d-9.1476043!16s%2Fg%2F11bw4hm49n?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Carmo+Archaeological+Museum/@38.7120383,-9.1406129,17z/data=!3m2!4b1!5s0xd19347f4bd8b7d7:0xd780cc121205771!4m6!3m5!1s0xd19347f372ec63f:0x32d7f56592e02cef!8m2!3d38.7120383!4d-9.1406129!16zL20vMGdxNG41?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ocean%C3%A1rio+de+Lisboa/@38.7635435,-9.0937415,17z/data=!3m2!4b1!5s0xd193183bcd49a59:0xb0ca6ccb4d0e350b!4m6!3m5!1s0xd193183750e5809:0x983f2e673a62e130!8m2!3d38.7635435!4d-9.0937415!16zL20vMDZjcTh2?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Tuk+Tuk+Lisbon+Tours/@38.715829,-9.141182,17z/data=!3m1!4b1!4m6!3m5!1s0xd23378052d2e7f9:0x7ec59c02711c4f04!8m2!3d38.715829!4d-9.141182!16s%2Fg%2F11r7x_yv5p?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bar+Alimentar/@38.7142631,-9.1528856,17z/data=!3m1!4b1!4m6!3m5!1s0xd1933000426b873:0x184a8e41dad28852!8m2!3d38.7142631!4d-9.1528856!16s%2Fg%2F11vwj_1fwb?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bessa+Restaurante(seafood+restaurant+))/@38.7130701,-9.1372625,17z/data=!3m1!4b1!4m6!3m5!1s0xd1934784d5317f7:0xfddfc41a3497d2ba!8m2!3d38.7130701!4d-9.1372625!16s%2Fg%2F11d_8dkz9c?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Machimbombo/@38.7109017,-9.1476882,17z/data=!3m1!4b1!4m6!3m5!1s0xd19352cb6d08caf:0x3e996c4718e4e75!8m2!3d38.7109017!4d-9.1476882!16s%2Fg%2F11h7d7xsf3?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Ursa+Beach/@38.9856969,-10.2212466,8.66z/data=!4m6!3m5!1s0xd1edcc6a318990b:0x629a9db069fbc2de!8m2!3d38.7905562!4d-9.4922968!16s%2Fg%2F121lyxnq?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 86,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)