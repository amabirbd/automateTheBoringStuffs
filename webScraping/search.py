# type in the word you wanna search in pypi and press enter 
# it will open first 5 results in the browser

import requests, webbrowser, bs4

search = input('search something: ')
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + search)
print(res.url)
res.raise_for_status()

# retreive top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each
linkElems = soup.select('.package-snippet')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)