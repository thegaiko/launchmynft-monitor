from pprint import pprint
import re
import requests
import json

def getLastCollection():
    url = "https://search.launchmynft.io/indexes/collections/search"

    payload = json.dumps({
    "facetsDistribution": [
        "type"
    ],
    "attributesToCrop": [
        "description:50"
    ],
    "filter": [
        "soldOut = false"
    ],
    "attributesToHighlight": [
        "*"
    ],
    "limit": 200,
    "sort": [
        "fractionMinted:desc"
    ],
    "q": ""
    })
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.launchmynft.io',
    'Referer': 'https://www.launchmynft.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Meili-API-Key': '3ee2cafe84ad0f0a28b2e8aea31df1f0e7adeed45973b24f0ab60307da150383',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()['hits'][0]

    return response