import re
import urllib.request

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')

for line in stream:
    decoded = line.decode('UTF-8').strip()

