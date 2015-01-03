import urllib2

cookievar="_ga=GA1.2.1522730967.1420254067; _gat=1; s=463tq8tqjgerdv0erj70rdgcd7; "
spoof_header = {
    # "Host": "www.prox4you.com",
    #"Accept": "image/webp,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, sdch",
    # "Accept-Language": "en-US,en;q=0.8",
    "Cookie": cookievar,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
}

def request(url):
    if not ("http://" in url or "https://" in url):
        url = "http://" + url
    url = urllib2.quote(url)
    url = url.replace("/", "%2F")
    url = "http://www.prox4you.com/browse/browse.php?u={}&b=20&f=norefer".format(url)
    request = urllib2.Request(url, headers=spoof_header)
    return urllib2.urlopen(request)

def addcookie(k, v):
    global cookievar
    cookievar += "{}={}; ".format(k, v)

def link(rel):
    url = "http://www.prox4you.com/" + rel
    request = urllib2.Request(url, headers=spoof_header)
    return urllib2.urlopen(request)
