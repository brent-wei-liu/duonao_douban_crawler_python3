import re
import os
files = []
for r, d, f in os.walk('douban'):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))

for doubanHtmlFile in files:
    print(f)
    html = []
    with open(doubanHtmlFile, 'r') as f:
        for cnt, line in enumerate(f):
            html.append(line.strip())
    html = ' '.join(html)
    print(html)
    titleRegex = 'class="title">.*?>(.*?)<\/a>'
    titles = []
    for idx, title in enumerate(re.findall(titleRegex, html)):
        print(idx)
        print(title)
        titles.append(title)

    with open('titles/%d.txt' % i, 'w') as f:
        for title in titles:
            f.write(title+'\n')
        f.flush()
