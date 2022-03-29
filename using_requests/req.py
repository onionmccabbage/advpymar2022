# to make calls to API end-points we need the requests library
import requests # we may need to pip install requests (or python -m pip install requests)

def makeCall():
    whichId = input('id? ')
    # this is a REST API - represents the state in the URL of the API
    url = 'https://jsonplaceholder.typicode.com/photos/{}'.format(whichId)
    try:
        response = requests.get(url) # get or post or put or update or delete ... all supported
        print(type(response))
        # we only want the returned json from the response object
        data = response.json() # or text() or html() or xml() ...
        print(data)
        # could also include 'url' and 'thumbnailUrl'
        print('Received {} {} {}'.format(data['albumId'], data['id'], data['title']))
    except Exception as err:
        print(err)
    finally:
        pass

if __name__ == '__main__':
    makeCall()