import os
import json
nameToId = {}

for root, dirs, files in os.walk('duonao/titles'):
    for id in files:
        with open('%s/%s' % (root, id), 'r') as file:
            name = file.read().strip()
            doubanJsonFileNames = 'douban/jsons/%s' % id
            nameToId[name] = (id, doubanJsonFileNames)

doubanScore = {}
for name, (id, doubanFileName) in nameToId.items():
    if not os.path.isfile(doubanFileName):
        continue
    with open(doubanFileName, 'r') as file:
        print(doubanFileName, name)
        obj = json.load(file)
        if obj['total'] == 0 or len(obj['subjects']) == 0:
            continue
        subject = obj['subjects'][0]
        url = subject['alt']
        title = subject['title']
        rating = subject['rating']['average']
        doubanScore[name] = {'url':url,
                             'title': title,
                             'rating': rating}

with open('douban/score.json', 'w') as f:
    json.dump(doubanScore, f, indent=4)
