import requests


# Saving Downloaded Files to the Hard Drive
# this downloads the whole text and saves it to 'RomeoAndJuliet' 
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()