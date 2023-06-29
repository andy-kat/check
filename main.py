import urllib.request
import re
url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"
response = urllib.request.urlopen(url)
data = response.read()
s = data.decode()
bbb = r'.*?(\d{2,3}).*?(\d{2,3}).*?(\d{2}).*?(\d{2})'
for line in s.split('\n'):
    if re.match(bbb, line):
        print('правильно написано')
       
    else:
        print('нетэ')