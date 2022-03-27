import requests

BASE = 'https://render-tron.appspot.com/screenshot/'
url = input("please enter url")
path = 'target.jpg'

response = requests.get(BASE + str(url), stream=True)
# save file, see https://stackoverflow.com/a/13137873/7665691
if not response.status_code == 200:
    print('URL INVALID!!!')
with open(path, 'wb') as file:
    for chunk in response:
        file.write(chunk)