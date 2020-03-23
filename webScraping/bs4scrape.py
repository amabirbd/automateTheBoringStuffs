import requests, bs4

"""
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(elems)
"""


# Finding an Element with the select() Method
"""
soup.select('div')

    All elements named <div>

soup.select('#author')

    The element with an id attribute of author

soup.select('.notice')

    All elements that use a CSS class attribute named notice

soup.select('div span')

    All elements named <span> that are within an element named <div>

soup.select('div > span')

    All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')

    All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')

    All elements named <input> that have an attribute named type with value button
"""

print('\n')
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select(('#author'))
print(type(elems))
print(len(elems))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

# getting all the paragraphs
para = exampleSoup.select('p')
print(para)
for i in para:
    print(i.getText().strip())


# Getting Data from an Element’s Attributes
spanElem = exampleSoup.select('span')[0]
print(spanElem)
print(spanElem.get('id'))
print(spanElem.attrs)