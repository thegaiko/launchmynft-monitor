import requests

url = "https://discord.com/api/webhooks/1020759277532627056/1eNo9K7OMaFXVcemgWylx6Quh1YLMjV3kX4azz9YgVMl2tQnwXWy28XRzL2O5ItA4Wrd"

def ifNull(x):
  try:
    return x
  except KeyError:
    return '-'

def timeConvert(x):
    year = int(f'{x[0]}{x[1]}{x[2]}{x[3]}')
    month = int(f'{x[5]}{x[6]}')
    day = int(f'{x[8]}{x[9]}')
    hour = int(f'{x[11]}{x[12]}')
    min = int(f'{x[14]}{x[15]}')
    sec = int(f'{x[17]}{x[18]}')
    return(f'{day}.{month}.{year} - {hour}:{min}:{sec}')

def sendHook(x):
    maxSupply = x['maxSupply']
    totalMints = x['totalMints']
    owner = x['owner']
    id = x['id']
    link = f'https://www.launchmynft.io/collections/{owner}/{id}'   
    
    collectionName = ifNull(x['collectionName'])
    type = ifNull(x['type'])
    description = ifNull(x['description'])
    data = {
        "username" : "LMNFT"
    }
    data["embeds"] = [
        {
      "title": "Launchmynft new collection",
      "color": 16087355,
      "fields": [
        {
          "name": "Collection name:",
          "value": collectionName,
          "inline": True
        },
        {
          "name": "Type:",
          "value": type,
          "inline": True
        },
        {
          "name": "Description:",
          "value": description
        },
        {
          "name": "Total mints:",
          "value": f'{totalMints}/{maxSupply}',
          "inline": True
        },
        {
          "name": "Link",
          "value": f'[Link]({link})',
          "inline": True
        },
      ],
      "footer": {
        "text": "gaiko (@metagaiko)"
      },
      "image": {
        "url": ifNull(x['collectionBannerUrl'])
      }
    }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
    
