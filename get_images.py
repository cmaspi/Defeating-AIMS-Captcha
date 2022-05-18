import wget
from bs4 import BeautifulSoup
import urllib.request

# To make multiple connections at once
from threading import Thread

# AIMS portal url
url = "https://aims.iith.ac.in/aims/"


def images():
    # 50K is more than enough for our dataset.
    for _ in range(50000):

        # We are using the urllib library to visit the AIMS website
        # then we are extracting the html doc. That's something you
        # would see when you use inspect element
        webUrl = urllib.request.urlopen(url)
        
        # We convert the html document to string
        html_doc = str(webUrl.read())

        # BeautifulSoup is an excellent library for 
        # parsing html doc. Here, we look for the element with
        # id : appCaptchaLoginImg, and extract the src, which is the label of the image
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Error handling is important, as you can often get those while
        # trying to read the html doc, maybe the server doesn't send proper response
        # We can just ignore the instance when we have an issue
        # We will just revisit the website again.
        try:
            download = soup.find(id="appCaptchaLoginImg")['src']
        except:
            continue

        _ = wget.download("https://aims.iith.ac.in/"+download,out="images/")

# Running the same function on 8 threads to speed up the process
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
