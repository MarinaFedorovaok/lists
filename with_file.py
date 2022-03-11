import pycurl 
 
file = open('pycurl.md','wb') 

crl = pycurl.Curl() 
#crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide') 
crl.setopt(crl.URL, 'https://www.proxy-list.download/api/v1/get?type=http')
crl.setopt(crl.WRITEDATA, file) 
crl.perform() 
crl.close() 