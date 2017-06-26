#!/usr/bin/python
print "Content-type: text/html\n\n"
# -*- coding:Utf-8 -*-
import urllib2


url = "http://paris.lachainemeteo.com/meteo-france/ville/previsions-meteo-paris-3903-0.php"
data=urllib2.urlopen(url)
data = data.read()

start_parse = '<div class="tempe '
end_parse = '<div class="separateur"><!-- --></div>'
temperature, pictogramme = [], []

temp_data = [item.split(end_parse) for item in data.split(start_parse)[1:]]

start_parse = '<div class="picto">'
end_parse = '" />'
pict_data = [a for a in [item.split(end_parse) for item in data.split(start_parse)]]

pictogramme = [ pic.split('.png')[0] for pic in [item[0].split('/')[-1] for item in pict_data] ][1:16]

effet = []
for a in pictogramme:
    if a[0] == 'c':
        if '0000' in a:
            effet.append('soleil : ')
        else:
            effet.append('nuage : ')

    if a[0] == 'x' or a[0] == 'p':
        effet.append('pluie : ')


print pictogramme
print len(pictogramme)

for item in temp_data:
    temperature.append([temp.split('>')[-1] for temp in item[0].split('&deg;')[:2]])

data = [(a+b[0]+'/'+b[1]).replace(' ','%20') for a,b in zip(effet, temperature)][:7]

data = '%0a'.join(data)
print data

me = 'https://smsapi.free-mobile.fr/sendmsg?user=1023xxx&pass=mySuperPass&msg='
data = me+data
