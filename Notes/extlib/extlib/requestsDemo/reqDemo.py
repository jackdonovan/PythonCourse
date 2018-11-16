import requests
from pprint import pprint

def main():
    print('GET')
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    pprint(r.json()[0])

    print('POST')
    r = requests.post('https://httpbin.org/post', data = {'hello':'world'})
    print(r.text)

    # a bunch of other options ar supported
    r = requests.delete('https://httpbin.org/delete')
    r = requests.head('https://httpbin.org/get')
    r = requests.options('https://httpbin.org/get')

    print('URL Parmeters')
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', params=payload)
    print(r.url)
    # any key with a vlue of None will not be added

    # lists of values will also work 
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('https://httpbin.org/get', params=payload)
    print(r.url)

    # response content will automaticlly be decoded
    r = requests.get('https://api.github.com/events')
    # print(r.text)
    # We can check what encoding was used.
    print(r.encoding)
    # we can also change what we would like it decoded as. This will
    # take effect whenever we call r.text
    r.encoding = 'ISO-8859-1'
    
    # we can also deal with binary content
    r = requests.get('https://dsu.edu/assets/uploads/general/_567x374/jenny-schulte.jpg')
    from PIL import Image
    from io import BytesIO
    i = Image.open(BytesIO(r.content))
    i.show()

    # you can modify headers
    headers = {'user-agent': 'mikesstuff/0.0.1'}
    r = requests.get('https://api.github.com/events', headers=headers)

    # File upload is a thing
    files = {'file': open('fish.png', 'rb')}
    r = requests.post('https://httpbin.org/post', files = files)


    # and so much more!

if __name__ == '__main__':
    main()