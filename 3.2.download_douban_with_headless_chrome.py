import pychrome
from urllib.parse import urlencode, quote_plus

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")
# create a tab
tab = browser.new_tab()
# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

def download(title):
    params = {'search_text': title, 'cat': 1002}
    paramsEncoded = urlencode(params, quote_via=quote_plus)
    url = 'https://movie.douban.com/subject_search?%s' % paramsEncoded
    url = 'https://movie.douban.com'

    print(url)
    tab.Page.navigate(url=url, _timeout=10)
    tab.wait(5)
    html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
    tab.wait(5)

    with open('douban/%s.html' % title, 'w') as f:
        f.write(html['result']['value'])
        f.flush()

    '''
    with io.open('douban/%s.html' % title, 'w', encoding='utf8') as f:
        # json.dump(obj, f, ensure_ascii=False, indent='  ')
        f.write(html)
        f.flush()
    '''

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab
tab.start()
tab.Network.enable()

for i in range(1, 5):
    with open('titles/%d.txt' % i, 'r') as f:
        for cnt, line in enumerate(f):
            title = line.strip()
            download(title)


# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()
# close tab
browser.close_tab(tab)
