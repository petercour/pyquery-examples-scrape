from pyquery import PyQuery as pq

doc =pq(url = "https://dev.to")

for link in doc('img'):
    print(link.attrib['src'])
