import urllib2
import json
import time

def sendSparkGET(url):
    request = urllib2.Request(url,
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    response = urllib2.urlopen(request)
    return response

bearer = "BEARER_TOKEN_HERE"

while True:
    try:
        result = sendSparkGET('https://api.ciscospark.com/v1/rooms')
        print result.code, time.time(), result.headers['Trackingid']
    except urllib2.HTTPError as e:
        if e.code == 429:
            print 'code', e.code
            print 'headers', e.headers
            print 'Sleeping for', e.headers['Retry-After'], 'seconds'
            sleep_time = int(e.headers['Retry-After'])
            while sleep_time > 10:
                time.sleep(10)
                sleep_time -= 10
                print 'Asleep for', sleep_time, 'more seconds'
            time.sleep(sleep_time)
        else:
            print e, e.code
            break