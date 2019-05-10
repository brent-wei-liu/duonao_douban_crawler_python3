import pychrome

'''
alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
alias start_chrome_server="chrome --headless --disable-gpu --remote-debugging-port=9222"

$ start_chrome_server
$ chrome --headless --disable-gpu --remote-debugging-port=9222
'''

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")
# create a tab
tab = browser.new_tab()
# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab
tab.start()
# call method
tab.Network.enable()
# call method with timeout
metrics = open('log/1.metrics.log', 'w')

for i in range(1, 605):
    url = 'https://www.dnvod.tv/list?keyword=&star=&page=%d&pageSize=30' % i
    tab.Page.navigate(url=url, _timeout=5)
    # wait for loading
    tab.wait(5)
    html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
    #html = tab.Runtime.evaluate(expression='document.getElementsByClassName(\'title\')')

    with open('duonao/htmls/%d.html' % i, 'w') as f:
        f.write(html['result']['value'])
        f.flush()

# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()
# close tab
browser.close_tab(tab)
metrics.close()
