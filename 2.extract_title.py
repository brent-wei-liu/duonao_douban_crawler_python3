import re
uuid = 0
for i in range(1, 605):
    html = []
    with open('duonao/htmls/%d.html' % i, 'r') as f:
        for cnt, line in enumerate(f):
            html.append(line.strip())
    html = ' '.join(html)
    titleRegex = 'class="title">.*?>(.*?)<\/a>'
    for idx, title in enumerate(re.findall(titleRegex, html)):
        print('%d\t%s' %(uuid, title))
        assert len(title) != 0, 'title len error!'
        with open('duonao/titles/%d' % uuid, 'w') as f:
            f.write(title+'\n')
            f.flush()
        uuid += 1
