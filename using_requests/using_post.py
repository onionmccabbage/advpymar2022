import requests
# to make a PSOT request we pass a payload of data
def makePost():
    url = 'https://httpbin.org/post' # a free echo-service
    payload = {'item':'Ocelot', 'status':'admin'}
    try:
        res = requests.post(url, data = payload)
        # did we receive a response?
        print(res.text)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makePost()