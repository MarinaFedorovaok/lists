import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'https://openproxy.space/api')

c.setopt(c.HTTPPOST, [
    ('fileupload', (
        c.FORM_BUFFER, 'readme.txt',
        c.FORM_BUFFERPTR, 'This is a fancy readme file',
    )),
])
c.perform()
c.close()