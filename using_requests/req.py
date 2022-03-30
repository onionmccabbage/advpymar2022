# to make calls to API end-points we need the requests library
import requests # we may need to pip install requests (or python -m pip install requests)
import sys # we may need to access some sys.argv

def makeCall(category='albums', id=3): # ...in case this module is importe and used elsewhere!
    # whichId = input('id? ')
    # this is a REST API - represents the state in the URL of the API
    url = 'https://jsonplaceholder.typicode.com/{}/{}'.format(category, id)
    try:
        response = requests.get(url) # get or post or put or update or delete ... all supported
        print(type(response))
        # we only want the returned json from the response object
        data = response.json() # or text() or html() or xml() ...
        print(data)
        # could also include 'url' and 'thumbnailUrl'
        # print('Received {} {} {}'.format(data['albumId'], data['id'], data['title']))
        # we can iterate over the returned dictionary of data
        for item in data:
            print(item, data[item])
    except Exception as err:
        print(err)
    finally:
        pass

if __name__ == '__main__':
    # check to see if any aditional arguments were passed as sys.argv
    if len(sys.argv) > 1:
        category = sys.argv[1]
        id       = sys.argv[2]
    else:
        category = 'photos'
        id       = 3
    makeCall(category, id)