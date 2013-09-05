import urllib
import re
 
url = "http://checkip.dyndns.org"
request = urllib.urlopen(url).read()
theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
print "Your IP Address is: ",  theIP
