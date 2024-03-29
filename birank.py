import json
import time
import requests

try:
    ts = str(int(time.time()))
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=39ab75b8d7ca520ee66f66c716050e8f&wts={}'.format(
        ts)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers = header)
    req.raise_for_status()
    obj = json.loads(req.text)
    for i in obj['data']['list']:
        print('|--' + i['title'])
        print('|---' + i['tname'])
        print('|----' + str(i['videos']))
        print('|-----' + i['short_link_v2'])
        print()
except requests.RequestException as e:
    print(e)
