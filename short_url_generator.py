import random
import string
d={}


def getshorturl(long_url):
    l=random.randint(6,10)
    chars=string.ascii_lowercase+string.ascii_uppercase+string.digits
    a=''
    shorturl=[]
    for i in range(0,l):
        a=random.choice(chars)
        shorturl.append(a)
    print(shorturl)
    shorturl="".join(shorturl)
    
    
    if shorturl in d:
        return getshorturl(long_url)
    else:
        d[shorturl]= long_url
        
    r="https://www.tinyurl.com/"+shorturl
    return r


def getlongurl(r):
    k=r[:24]

    if k in d:
        return d[k]
    else :
        return None
    
  