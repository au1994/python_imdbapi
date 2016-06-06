import requests
import sys,traceback
from bs4 import BeautifulSoup

def imdb_rating(movie):
    url = "http://www.imdb.com/find?s=tt&q="+movie
    print "Searching on %s" % url
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        print "Unable to connect"
        raise SystemExit("Slow internet connection")
    soup = BeautifulSoup(r.content,"html.parser")
    total = soup.find_all("td", {"class":"result_text"})
    #print len(total)
    if len(total)==0:
        print "No results found"
        sys.exit()
    for item in total:
        title = item.get_text().strip()
        print "Title %s" % title
        url = item.find("a").get("href")
        url = "http://www.imdb.com"+url
        print "URL %s" % url 
        print "\n"


                

        


if __name__ == '__main__':
    print "Enter the movie name"
    movie = raw_input()
    #movie = "fight club"
    #print movie
    imdb_rating(movie)

        
