import pycurl
from io import BytesIO

buffer = BytesIO()
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

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
#print(body.decode('iso-8859-1'))