# cofing: utf-8

import urllib2

request = 'http://www.baidu.com'
reponse = urllib2.urlopen(request)
print reponse.read()
