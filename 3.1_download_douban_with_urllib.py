import urllib.request
import urllib.parse
import json
import os
import io
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
        params = urllib.parse.urlencode({'q': title, 'start': 0, 'count': 10})
        #url = "https://api.douban.com/v2/movie/search?%s" % params
        url = "https://douban.uieee.com/v2/movie/search?%s" % params

        print(url)
        with urllib.request.urlopen(url) as response:
            status = response.status
            headers = dict(response.info().items())
            remain = headers['X-Ratelimit-Remaining2']
            print('status: %s\tX-Ratelimit-Remaining2 : %s' %(status, remain))
            jsonText = response.read().decode('utf-8')
            # obj = json.loads(html)
            with io.open('douban/jsons/%d' % uuid, 'w', encoding='utf8') as file:
                # json.dump(obj, f, ensure_ascii=False, indent='  ')
                file.write(json.dumps(json.loads(jsonText), sort_keys=True, indent=4))
                file.flush()
        if int(remain) < 1000:
            time.sleep(600)
        else:
            time.sleep(1)
        #break
