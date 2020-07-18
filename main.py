from lxml import etree
import urllib3
from urllib.parse import quote
from re import search

def encode_url(url):
    return quote(url, safe='')

def similar_page(url):
    # specify the yandex part and image url
    req = ("https://yandex.com/images/search?url=", "&rpt=imageview")

    # encode img url and create yandex url
    enc_url = encode_url(url).join(req)

    # send get request
    # http = urllib3.PoolManager()
    http = urllib3.ProxyManager("http://81.201.60.130:80/")

    r = http.request('GET', enc_url)

    rr = r.data.decode()
    print(len(rr))

    # m = search(r'href="(/images/search\?cbir_id=\S+&rpt=imagelike)"', rr)
    m = search(r'href="(/images/search\?cbir_id=\S+rpt=imagelike)"', rr)
    mm = m[1].replace('&amp;', '&')
    ss = search('/images/search\?cbir_id=\S+rpt=imagelike', mm)

    return 'https://yandex.com' + ss[0]

# # write html to file
with open("output1.html", "w") as file:
    file.write(str(rr))

