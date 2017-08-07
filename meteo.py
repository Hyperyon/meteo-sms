#!/usr/bin/python
print "Content-type: text/html\n\n"
# -*- coding:Utf-8 -*-

import urllib2 as get

api = "https://smsapi.free-mobile.fr/sendmsg?user=1023xxx&pass=mySuperPass&msg="
site = 'http://paris.lachainemeteo.com/meteo-france/ville/previsions-meteo-paris-3903-0.php'
req = get.build_opener()

def get_data():
    data = req.open(site).read()
    data = data.split('<img infoPrincipale="1" alt="')[1:4]

    for i, element in enumerate(data):
        a = element.split('&deg</div>')[0]
        temps = a.split('"')[0]
        temperature = a.split('>')[-1]
        data[i] = temperature +'°C '+ temps

    return '%0A'.join(data) #%0A saut de ligne

def send_payload(data):
    req.open(api+data)

send_payload(get_data())
