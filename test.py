from pyquery import PyQuery as pq

date = "2019-07-14"
doc =pq(url = "https://news.ycombinator.com/front?day=" + date )

links = []
for link in doc('a.storylink'):
    links.append(link.attrib['href'])

with open('output.csv','w+') as csvfile:
    for link in links:
        link = link.replace(";","")
        csvfile.write( date + ";" + link + ";" )
        csvfile.write('\n')
                    
