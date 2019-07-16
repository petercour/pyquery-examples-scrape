from pyquery import PyQuery as pq

doc =pq(url = "https://pythonbasics.org")
print( doc('title').text() )
