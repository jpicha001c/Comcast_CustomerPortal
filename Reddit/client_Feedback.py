__author__ = '289085'


#url1 = "https://www.reddit.com/r/Comcast/comments/4n0ssg/worst_experience_ofmy_whole_life_another_one/d4b7uig"
#url2 = "https://www.reddit.com/r/Comcast/comments/?count=25&after=t1_d49b159"
#f= open("gg.txt",'rb')
#id = f.read()
#url =url2.rsplit('/',2)

import urllib2, json,time
try:
    url = "http://www.reddit.com/r/comcast/comments/4oavph.json?"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    time.sleep(180)
    trends = data[0]['data']
    print trends
except urllib2.HTTPError as e:
    print (e.code)



