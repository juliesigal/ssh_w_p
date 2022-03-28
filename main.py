import requests
from InvalidUrlException import InvalidUrlException

BASE = 'https://render-tron.appspot.com/screenshot/'
path = 'target.jpg'

try:
    url = input("please enter url")
    response = requests.get(BASE + str(url), stream=True)

       # check if url valid:

    if not response.status_code == 200:
        raise InvalidUrlException
except InvalidUrlException as e:
    print(e)

    # save file:
else:
    with open(path, 'wb') as file:
        for chunk in response:
            file.write(chunk)


