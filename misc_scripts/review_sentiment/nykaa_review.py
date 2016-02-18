import sys
import urllib2
import string
from bs4 import BeautifulSoup as bs

POSITIVE_FILE = "/home/vatsala/py-scripts/misc_scripts/review_sentiment/positive.txt"
NEGATIVE_FILE = "/home/vatsala/py-scripts/misc_scripts/review_sentiment/negative.txt"

def extract_reviews(url):
    html_doc = urllib2.urlopen(url)
    soup = bs(html_doc.read(), 'html.parser')
    review_head = [str(review.findAll('p')[0].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    review_content = [str(review.findAll('p')[1].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    return {'review_head': review_head, 'review_content': review_content}

def get_file_data(filename):
    inFile = open(filename, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    inFile.close()
    return wordlist

def get_sentiment_list():   
    print "senti"
    positive = get_file_data(POSITIVE_FILE)
    negative = get_file_data(NEGATIVE_FILE)
    return {'positive': positive , 'negative': negative}

if __name__ == '__main__':
    url = 'http://www.nykaa.com/bath-and-body/nivea-body-lotion-extra-whitening-cell-repair-uv-protect-vit-c.html?root=catg_Nykaas%20Choice&ptype=product&brand=catg_nykaas+choice'
    try:
        reviews = extract_reviews(url)
        if len(reviews['review_head']) != 0:
            sentiment_map = get_sentiment_list()
            print sentiment_map
        else:
            print "Either this product has no reviews or this is not a valid product page"
    except:
        print "Unknown/Incorrect url! Please try with a different one"
        sys.exit()
    print reviews