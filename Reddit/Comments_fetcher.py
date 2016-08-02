__author__ = '262844'
import urllib2
import re,time,json
from BeautifulSoup import BeautifulSoup
from tornado import ioloop, httpclient
i =0



def handle_request(response):
    global i
    print "---i--->>",i
    print response.effective_url
    #print "len of url--",len(response.effective_url)
    #print response.body
    data = json.loads(response.body)
    if 'title' not in data[0]['data']['children'][0]['data']:
        print "title key not found"
    else:
        print "Title:",data[0]['data']['children'][0]['data']['title']

    print "selftext:",data[0]['data']['children'][0]['data']['selftext']
    print "Time:", data[0]['data']['children'][0]['data']['created_utc']
    print "Comment_count:", data[0]['data']['children'][0]['data']['num_comments']
    for j in range (len(data[1]['data']['children'])):
        print "---",data[1]['data']['children'][j]['data']['body']
        #print "reddit_cooment_Time:", data[1]['data']['children'][j]['data']['created_utc']
    #time.sleep(60)
    print "---------------------------------------------------------------"
    i -= 1
    #print "---i---",i
    if i == 1:
        print "stoop---"
        ioloop.IOLoop.instance().stop()
        pass



def reddit_check():
    global i
    print "Inside comcast_reddit"
    url_list =[]
    reddit_comments=[]
    sort_uri=[]
    url = "http://www.reddit.com/r/comcast/comments/"
    headers = {'Content-Type': 'application/xml'}
    req = urllib2.Request(url,headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    response =urllib2.urlopen(req)
    #data = json.loads(response.read())
    data = response.read()
    f =open('data.txt','wb')
    f.write(data)
    f1 = open('data.txt','rb')
    href1 = f1.read()
    soup = BeautifulSoup(href1)
    for link in soup.findAll('a',attrs={'href': re.compile("^https://www.reddit.com/r/Comcast/comments/")}):
        link = link.get('href')
        #time.sleep(3)
        id1 = link.rsplit('/', 3)[1]
        #print id1
        comment = "http://www.reddit.com/r/comcast/comments/"+id1+ ".json?"
        reddit_comments.append(comment)
    print "---reddit comments",len(reddit_comments)
    f2 = open('datajson.txt','wb')
    for uri in reddit_comments:
        uri=uri.strip()
        url_list.append(uri)
    sortdata = list(set(url_list))
    #print "--sort--",type(sortdata)
    print "sore --",len(sortdata)
    for i in sortdata:
        if str(i) == "http://www.reddit.com/r/comcast/comments/Comcast.json?":
            sortdata.remove("http://www.reddit.com/r/comcast/comments/Comcast.json?")
    print "Sortdata_original",len(sortdata)
    for reddit_uri in sortdata:
        f2.write("%s\n" % reddit_uri)
    f2.close()

    if len(sortdata)!=0:
        print " Calling datajson..."

        http_client = httpclient.AsyncHTTPClient()
        #for url in open('datajson.txt'):
        i = 0
        for url in open('datajson.txt'):
            #print "--url--",url
            i += 1
            print "---http i--",i

            http_client.fetch(url.strip(), handle_request,method='GET')
        ioloop.IOLoop.instance().start()



    else:
        print "empty... "


'''

def handle_request(response):
    print response.effective_url
    #print response.body
    data = json.loads(response.body)
    if 'title' not in data[0]['data']['children'][0]['data']:
        print "title key not found"
    else:
        print "Title:",data[0]['data']['children'][0]['data']['title']

    print "selftext:",data[0]['data']['children'][0]['data']['selftext']
    print "Time:", data[0]['data']['children'][0]['data']['created_utc']
    for j in range (len(data[1]['data']['children'])):
        print "---",data[1]['data']['children'][j]['data']['body']
    #print "Time:", data[0]['data']['children'][0]['data']['created_utc']
    #time.sleep(60)
    print "---------------------------------------------------------------"
    global i
    i -= 1
    if i == 0:
        ioloop.IOLoop.instance().stop()

def http_call():
    http_client = httpclient.AsyncHTTPClient()
    #for url in open('datajson.txt'):
    for url in open('datajson.txt'):
        #print "--url--",url
        i += 1
        http_client.fetch(url.strip(), handle_request,method='GET')
    ioloop.IOLoop.instance().start()
'''



