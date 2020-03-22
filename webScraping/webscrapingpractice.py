import webbrowser
import requests



res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res)
print(type(res))
print(res.status_code)
# List of all http status could be found here : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

print(res.apparent_encoding)
print(res.text[:250])
print('length of the text:', len(res.text))

resErr = requests.get('https://inventwithpython.com/page_that_does_not_exist')

# this will raise error if download fails
#resErr.raise_for_status()

# with try except
#try:
#    resErr.raise_for_status()
#except Exception as exc:
#    print('There was a problem: %s' % (exc))

