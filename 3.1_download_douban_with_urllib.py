import urllib.request
import urllib.parse
import json
import os
import io
from random import shuffle
import time
if __name__ == '__main__':
    titles = {}
    for root, dirs, files in os.walk("duonao/titles/", topdown=False):
        for name in files:
            path = os.path.join(root, name)
            with open(path, 'r') as f:
                title = f.read().strip()
                uuid = int(name)
                titles[uuid] = (path, title)
    for uuid in sorted(titles.keys()):
        path, title = titles[uuid]
        print(uuid, titles[uuid])
        doubanUrl = 'https://api.douban.com/v2/movie/search'
        params = urllib.parse.urlencode({'q': title, 'start': 0, 'count': 10})
        url = "https://api.douban.com/v2/movie/search?%s" % params
        print(url)
        with urllib.request.urlopen(url) as f:
            jsonText = f.read().decode('utf-8')
            # obj = json.loads(html)
            with io.open('douban/jsons/%d' % uuid, 'w', encoding='utf8') as f:
                # json.dump(obj, f, ensure_ascii=False, indent='  ')
                f.write(jsonText)
                f.flush()
        time.sleep(2)
