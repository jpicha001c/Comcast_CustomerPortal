__author__ = '289085'
'''
https://www.reddit.com/r/comcast/comments/
$.getJSON("http://www.reddit.com/r/" + sub + "/comments/" + id + ".json?", function (data){
  $.each(data[1].data.children, function (i, item) {
    var comment = item.data.body
    var author = item.data.author
    var postcomment = '<p>[Author]' + author + '<br>' + comment + '</p>'
    results.append(postcomment)
  });
});
'''
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import time
list1=[]
url ="http://www.reddit.com/r/comcast/comments/"
response = urllib2.urlopen(url)
data = response.read()
f =open('data.txt','wb')
f.write(data)
f1 = open('data.txt','rb')
href1 = f1.read()
soup = BeautifulSoup(href1)
for link in soup.findAll('a',attrs={'href': re.compile("^https://www.reddit.com/r/Comcast/comments/")}):
    link = link.get('href')
    time.sleep(3)
    id1 = link.rsplit('/', 3)[1]
    print id1
    comment = "http://www.reddit.com/r/comcast/comments/"+id1+ ".json?"
    print comment

#print list1
#d = soup.findAll('a', attrs={'href': re.compile("^https://www.reddit.com/r/Comcast/comments/")})
#print "---",d