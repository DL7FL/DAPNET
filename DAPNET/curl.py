## curl -H "Content-Type: application/json" -X POST -u USER:PASSWORD -d '{ "text": "FUNKRUFTEXT", "callSignNames": ["RUFZEICHEN"], "transmitterGroupNames": ["SENDERGRUPPENNAME"], "emergency": false }' URL/calls
## http://www.hampager.de:8080

import pycurl

from urllib.parse import urlencode


c = pycurl.Curl()
c.setopt(c.URL, '127.0.0.1/index.php')

post_data =  {'text': 'testtext', 'callSignNames': 'DL7FL', 'transmitterGroupNames': 'all', 'emergency': 'false'}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)

c.perform()
c.close()