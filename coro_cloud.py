import requests
import json

url = 'https://api.yimian.xyz/coro'
data = requests.get(url).text

city_dict = {}
json_data = json.loads(data)
# print(json_data)
# print(json_data)
for p in json_data:
    if 'cities' in p:
        for c in p['cities']:
            cityName = c['cityName']
            cCount = c['confirmedCount']
            sCount = c['suspectedCount']
            total = int(cCount) + int(sCount)
            city_dict[cityName] = total
    else:
        cityName = p['provinceName']
        cCount = p['confirmedCount']
        sCount = p['suspectedCount']
        total = int(cCount) + int(sCount)
        city_dict[cityName] = total

# print(city_dict)
    with open('city_count.txt','w') as f:
         for k, v in city_dict.items():
             f.write(f"{k}:{v}\n")


import wordcloud
import matplotlib.pyplot as plt

# ccloud = wordcloud.W

