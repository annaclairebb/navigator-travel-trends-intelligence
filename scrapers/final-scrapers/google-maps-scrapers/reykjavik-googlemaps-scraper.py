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
    "&limit_per_input=97"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Hallgrimskirkja/@64.1420229,-21.9265493,17z/data=!3m1!4b1!4m6!3m5!1s0x48d674cca0432db5:0xf7af28c4489daaef!8m2!3d64.1420229!4d-21.9265493!16s%2Fg%2F1tknk0hk?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Blue+Lagoon/@63.8807176,-22.4472964,17z/data=!3m1!4b1!4m6!3m5!1s0x48d61d66aff7df0d:0xf3747a894416f06e!8m2!3d63.8807176!4d-22.4472964!16zL20vMDdranE2?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Sky+Lagoon/@64.1103143,-22.0415396,11.81z/data=!4m6!3m5!1s0x48d60b86ce2825a7:0x2abad76345ba6910!8m2!3d64.1164891!4d-21.9462908!16s%2Fg%2F11lt31jbvq?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Harpa+Concert+Hall+and+Conference+Centre/@64.1561117,-21.9611829,13.3z/data=!3m1!5s0x48d674d304183cfd:0xe4e452f87a590a78!4m6!3m5!1s0x48d675a9d316864b:0xc1f29c378b85e65b!8m2!3d64.1502464!4d-21.9322804!16s%2Fg%2F12q4tv44j?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Sk%C3%B3lav%C3%B6r%C3%B0ust%C3%ADgur+Rainbow+Street/@64.1561117,-21.9611829,13.3z/data=!4m6!3m5!1s0x48d6759540b92add:0x591dd913dbbce787!8m2!3d64.146022!4d-21.9325495!16s%2Fg%2F11j7hmxhy9?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Sun+Voyager/@64.1476306,-21.9222846,17z/data=!3m1!4b1!4m6!3m5!1s0x48d674ce090ce6cf:0xd87b3a7b999ca6a8!8m2!3d64.1476306!4d-21.9222846!16s%2Fm%2F0bbth05?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3Dhttps://www.google.com/maps/place/Perlan/@64.1292528,-21.9188709,17z/data=!3m1!4b1!4m6!3m5!1s0x48d60b4cb9a4739d:0x720effd6596f3f29!8m2!3d64.1292528!4d-21.9188709!16zL20vMDk5dnkw?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Perlan/@64.1292528,-21.9188709,17z/data=!3m1!4b1!4m6!3m5!1s0x48d60b4cb9a4739d:0x720effd6596f3f29!8m2!3d64.1292528!4d-21.9188709!16zL20vMDk5dnkw?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Gullfoss+Falls/@64.3266938,-20.1204131,16z/data=!3m1!4b1!4m6!3m5!1s0x48d6a574af45b6c9:0x2c6347db0b411601!8m2!3d64.3270716!4d-20.1199478!16zL20vMDJnYzA2?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Laugavegur,+Reykjav%C3%ADk,+Iceland/@64.1430168,-21.9126348,17z/data=!3m1!4b1!4m10!1m2!2m1!1sLaugavegur!3m6!1s0x48d674cc4a0700eb:0xe8b90d6560c87172!8m2!3d64.1430168!4d-21.9126348!15sCgpMYXVnYXZlZ3VykgEObm90YWJsZV9zdHJlZXTgAQA!16zL20vMDNwX3pk?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Geysir/@64.3103282,-20.3022988,17z/data=!3m1!4b1!4m6!3m5!1s0x48d6a39f03424f3f:0xb4751c1a62e2283f!8m2!3d64.3103719!4d-20.3023605!16zL20vMDFzZjc4?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Black+Sand+Beach/@63.4166622,-19.0108431,17z/data=!3m1!4b1!4m6!3m5!1s0x48d74b0071dbbfb1:0x8b4b9a8002b2e3c8!8m2!3d63.4166622!4d-19.0108431!16s%2Fg%2F11w962hchy?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Thingvellir+National+Park/@64.2821725,-21.0764492,17z/data=!3m1!4b1!4m6!3m5!1s0x48d6811ffb13697b:0x6b756c8b079262f2!8m2!3d64.2821725!4d-21.0764492!16zL20vMDMxOXoy?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Sk%C3%B3gafoss/@63.5320124,-19.5113764,17z/data=!3m1!4b1!4m6!3m5!1s0x48d73b7639a58c15:0xf60c71fcdfe7948!8m2!3d63.5320523!4d-19.5113705!16zL20vMDMyZ2pi?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Seljalandsfoss/@63.6155984,-19.9885022,17z/data=!3m1!4b1!4m6!3m5!1s0x48d71eade8ef2415:0xae01e6205209178d!8m2!3d63.6156232!4d-19.9885688!16zL20vMDMyZ2tq?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/J%C3%B6kuls%C3%A1rl%C3%B3n/@64.0761875,-16.2092823,12z/data=!3m1!4b1!4m6!3m5!1s0x48cfd6ecd73a3819:0xcd05c959e10146a9!8m2!3d64.0784458!4d-16.2305537!16zL20vMDMydjRn?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Reynisfjara+Beach/@63.4052422,-19.0694762,13z/data=!3m1!4b1!4m6!3m5!1s0x48d74984d567267d:0xe07954a3f4b36bd5!8m2!3d63.4057404!4d-19.0716193!16s%2Fg%2F1tfg77rb?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Diamond+Beach/@64.0443336,-16.1776622,14z/data=!3m1!4b1!4m6!3m5!1s0x48cfd719a4fb06f3:0x4202e865f907845a!8m2!3d64.044334!4d-16.1776622!16s%2Fg%2F11bxdvx0kx?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/The+Icelandic+Phallological+Museum/@64.1484617,-21.9357702,17z/data=!3m1!4b1!4m6!3m5!1s0x48cd42159e4b2c3b:0x4dae8a9fbb2fe4a0!8m2!3d64.1484617!4d-21.9357702!16zL20vMDR6ZDl4?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/FlyOver+Iceland/@64.156511,-21.9485415,17z/data=!3m1!4b1!4m6!3m5!1s0x48d60b95b5ce05d7:0x6cc790c894748ee1!8m2!3d64.156511!4d-21.9485415!16s%2Fg%2F11g0h1wndk?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Harbor+in+Reykjavik/@64.1499249,-21.9417573,17z/data=!3m1!4b1!4m6!3m5!1s0x48d60b2cce2a248b:0x5bdf41c0f3ad1aec!8m2!3d64.1499249!4d-21.9391824!16s%2Fg%2F11b7cjxjqv?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Gr%C3%B3tta+Lighthouse/@64.16501,-22.0219814,17z/data=!3m1!4b1!4m6!3m5!1s0x48d60ae007d9e365:0xab8ecb00d897b53a!8m2!3d64.16501!4d-22.0219814!16s%2Fg%2F1tjpq29t?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Lebowski+Bar/@64.1456833,-21.9296444,17z/data=!3m1!4b1!4m6!3m5!1s0x48d674cd1388eeff:0xc80befcf06e33113!8m2!3d64.1456833!4d-21.9296444!16s%2Fg%2F1hhx4tr65?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 97,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)