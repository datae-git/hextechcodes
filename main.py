import requests
import json
import time

url = "https://us-central1-verizon-commonbackend-prod.cloudfunctions.net/getCouponCodes"
headers = {
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Chromium";v="111", "Not(A:Brand";v="8"',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Mobile": "?0",
    "Clientapikey": "8PuUVcyEU2jiUBMWygTdHQfDfJ5vTg3z",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Origin": "https://gaming.vz-experiences.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://gaming.vz-experiences.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}

data = {"id": "IsmBzrRajs5YDAC6ojHl"}

with open("codes.txt", "w") as file:
    for i in range(0, 100):
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_json = response.json()
        print("Attempting request # " + str(i))
        if response_json.get("success") and "coupons" in response_json:
            print("Request # " + str(i) + " success!")
            code = response_json["coupons"]["CONTENT_CODES"]
            file.write(f"{code}\n")
        else:
            print("Request # " + str(i) + " failed")
        time.sleep(2)
