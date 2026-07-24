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
            "url":"https://www.google.com/maps/place/Souk+Semmarine/@31.6280373,-7.988067,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee426bbaa7a7:0x4a1ed13e9aea3e1b!8m2!3d31.6280373!4d-7.988067!16s%2Fg%2F11bvt5mz96?entry=ttu&g_ep=EgoyMDI2MDcyMC4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Jardin+Majorelle/@31.6412031,-8.0032397,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee878b66b78f:0x88ccf6c9ced0f11c!8m2!3d31.6412031!4d-8.0032397!16zL20vMDQzNDdj?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Madrasa+Ben+Youssef/@31.6320537,-7.9884648,17z/data=!4m10!1m2!2m1!1sBen+Youssef+madrasa!3m6!1s0xdafee69803640af:0x5512adc5ece4a3a1!8m2!3d31.6320537!4d-7.9862761!15sChNCZW4gWW91c3NlZiBtYWRyYXNhWhUiE2JlbiB5b3Vzc2VmIG1hZHJhc2GSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16zL20vMDU5NmJ3?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Agafay+desert+best+camp/@31.6313834,-8.0559441,12.51z/data=!4m6!3m5!1s0xdafef510cb20ac9:0xee2198a1b2fea7eb!8m2!3d31.6235255!4d-8.0033446!16s%2Fg%2F11k4pnh2dq?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bahia+Palace/@31.6313834,-8.0559441,12.51z/data=!4m6!3m5!1s0xdafee4772c14bab:0x82985f4745817fdb!8m2!3d31.6217067!4d-7.9819688!16zL20vMDZmNGhr?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Jemaa+el-Fnaa/@31.6259521,-7.9890491,17z/data=!3m1!4b1!4m6!3m5!1s0xdafef41749d6bf9:0x72aec20ce3a1e60d!8m2!3d31.6259521!4d-7.9890491!16zL20vMDR5dnFs?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Yves+Saint+Laurent+Museum/@31.6425934,-8.0031422,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee7d7ade8727:0x51895eec21c72d37!8m2!3d31.6425934!4d-8.0031422!16s%2Fg%2F11c6t6tx_f?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Koutoubia/@31.6236766,-7.9935429,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee5c99d75ddf:0xd8cd38139a6e6fc2!8m2!3d31.6237205!4d-7.9936196!16zL20vMDZmNGRw?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Bacha+Coffee/@31.6236766,-7.9935429,17z/data=!4m6!3m5!1s0xdafefac82c777fd:0x1a677b7b36a83e7c!8m2!3d31.6310693!4d-7.9924865!16s%2Fg%2F11j080z48q?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/El+Badi+Palace/@31.6007694,-8.0687469,12.88z/data=!4m6!3m5!1s0xdafee4604ce6195:0xea9a85527a0e5a61!8m2!3d31.6182364!4d-7.9858623!16zL20vMDhkdzV3?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Le+Jardin+Secret/@31.6306908,-7.98952,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee684dbf3e01:0x50d89166ad205c0c!8m2!3d31.6306908!4d-7.98952!16s%2Fg%2F11cnbz2syh?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Palmeraie+Marrakech+chameau/@31.6767796,-8.002287,13.04z/data=!4m9!1m2!2m1!1spalmeraie+palace+marrakech!3m5!1s0xdafede69e10e07f:0x331e8b0d8932fd6c!8m2!3d31.6761438!4d-7.9664402!16s%2Fg%2F11t9t1tf9r?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Comptoir+Darna/@31.6238786,-8.0031521,17z/data=!3m1!4b1!4m6!3m5!1s0xdafeef58bf0cbfd:0x866d6609ee013e4a!8m2!3d31.6238786!4d-8.0031521!16s%2Fg%2F1vntl7bs?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/La+Mamounia/@31.6215239,-7.997488,17z/data=!3m1!4b1!4m9!3m8!1s0xdaff7726fca55af:0xe665ab0e7f26c957!5m2!4m1!1i2!8m2!3d31.6215239!4d-7.997488!16s%2Fm%2F0nhjdbq?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Dar+El+Bacha+Museum/@31.6320537,-7.9862761,17z/data=!4m6!3m5!1s0xdafefa99c22b083:0xe1c7a8c261407c3e!8m2!3d31.6314376!4d-7.9922895!16s%2Fg%2F11h4h33vj6?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Marrakech+Museum/@31.6316423,-7.9862131,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee6988fdf8cb:0x5f248cd3f7de7c66!8m2!3d31.6316423!4d-7.9862131!16zL20vMDg4cG01?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Nomad+Marrakech/@31.6285931,-7.9875304,17z/data=!3m1!4b1!4m6!3m5!1s0xdafee42094a4f09:0xd73943db8d0a0e50!8m2!3d31.6285931!4d-7.9875304!16s%2Fg%2F1q6jf00ly?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
        {
            "url":"https://www.google.com/maps/place/Menara+Gardens/@31.6143271,-8.0225425,17z/data=!3m1!4b1!4m6!3m5!1s0xdafeee649f63e07:0x5d8e3627f4ecc87e!8m2!3d31.6143271!4d-8.0225425!16s%2Fm%2F025zq65?entry=ttu&g_ep=EgoyMDI2MDcxOS4wIKXMDSoASAFQAw%3D%3D",
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