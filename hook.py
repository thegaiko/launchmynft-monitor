import requests

url = "https://discord.com/api/webhooks/1000115989880516808/n0wPo2dPqSC9sG0opW2yxu4_qwX3ObCHYWA9ngQ5f9ifHu3x1PnB1Y26aeKWM9eyOtso"

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
    data = {
        "username" : "Degen"
    }
    data["embeds"] = [
        {
      "title": "Launchmynft new collection",
      "color": 12910592,
      "fields": [
        {
          "name": "Collection name:",
          "value": x['collectionName'],
          "inline": True
        },
        {
          "name": "Type:",
          "value": x['type'],
          "inline": True
        },
        {
          "name": "Description:",
          "value": x['description']
        },
        {
          "name": "Launch date:",
          "value": timeConvert(x['launchDate']),
          "inline": True
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
        "text": "ARBIT",
        "icon_url": "https://sun9-58.userapi.com/impf/jgOkfU_yUf-HUS1_zd73z61ZpJZi1l6l6PxRjA/JtNJ-75JJtY.jpg?size=1624x1624&quality=95&sign=c4820a07df07b1312763693a050d833d&type=album"
      },
      "image": {
        "url": x['collectionBannerUrl']
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
    
