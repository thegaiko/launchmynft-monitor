from pprint import pprint
import re
import requests
import json

def getLastCollection():
    url = "https://s.launchmynft.io/multi_search?x-typesense-api-key=UkN4Vnd3V2JMWWVIRlFNcTJ3dng4VGVtMGtvVGxBcmJJTTFFYS9MNXp1WT1Ha3dueyJmaWx0ZXJfYnkiOiJoaWRkZW46ZmFsc2UiLCJleGNsdWRlX2ZpZWxkcyI6ImhpZGRlbiIsInF1ZXJ5X2J5IjoiY29sbGVjdGlvbk5hbWUsb3duZXIiLCJsaW1pdF9oaXRzIjoyMDAsInNuaXBwZXRfdGhyZXNob2xkIjo1MH0%3D"

    payload = "{\"searches\":[{\"query_by\":\"collectionName,owner\",\"per_page\":10,\"sort_by\":\"deployed:desc\",\"highlight_full_fields\":\"collectionName,owner\",\"collection\":\"collections\",\"q\":\"*\",\"facet_by\":\"soldOut,twitterVerified,type,cost\",\"filter_by\":\"soldOut:=[false] && twitterVerified:=[true]\",\"max_facet_values\":10,\"page\":1},{\"query_by\":\"collectionName,owner\",\"per_page\":1,\"sort_by\":\"deployed:desc\",\"highlight_full_fields\":\"collectionName,owner\",\"collection\":\"collections\",\"q\":\"*\",\"facet_by\":\"soldOut\",\"filter_by\":\"twitterVerified:=[true]\",\"max_facet_values\":10,\"page\":1},{\"query_by\":\"collectionName,owner\",\"per_page\":1,\"sort_by\":\"deployed:desc\",\"highlight_full_fields\":\"collectionName,owner\",\"collection\":\"collections\",\"q\":\"*\",\"facet_by\":\"twitterVerified\",\"filter_by\":\"soldOut:=[false]\",\"max_facet_values\":10,\"page\":1}]}"
    headers = {
    'authority': 's.launchmynft.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.launchmynft.io',
    'referer': 'https://www.launchmynft.io/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()['results'][0]['hits'][0]['document']

    return response
