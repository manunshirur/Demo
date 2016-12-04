import webbrowser, requests, sys, bs4

res = requests.get("https://www.google.com/search?q="+' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
    sys.exit()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    if("wikipedia" in str(linkElems[i])):
        webbrowser.open('http://google.com'+linkElems[i].get('href'))
