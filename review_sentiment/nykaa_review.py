import sys
import urllib2
import string
import re
import math
from bs4 import BeautifulSoup as bs

#tested largely on nykaa.com -> bath and body section
#sample url : http://www.nykaa.com/bath-and-body/bath/showergels/neutrogena-rainbath-refreshing-shower-and-bath-gel.html?root=catg&ptype=product

POSITIVE_FILE = "/home/vatsala/py-scripts/misc_scripts/review_sentiment/positive.txt"
NEGATIVE_FILE = "/home/vatsala/py-scripts/misc_scripts/review_sentiment/negative.txt"

#extracts review components from the product page
def extract_reviews(soup):
    review_head = [str(review.findAll('p')[0].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    review_content = [str(review.findAll('p')[1].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    return {'review_head': review_head, 'review_content': review_content}

#extracts overall rating for the product
def extract_rating(soup):
    rating = soup.find('div', class_ ='product-shop')
    p_container = rating.find('p', class_ ='reviews')
    return str(p_container.find('meta')['content']) 

#returns list of words in a file
def get_file_data(filename):
    inFile = open(filename, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    inFile.close()
    return wordlist

#returns a map of positive and negative words
def get_sentiment_list():   
    positive = get_file_data(POSITIVE_FILE)
    negative = get_file_data(NEGATIVE_FILE)
    return {'positive': positive , 'negative': negative}

#computes sentiment for a given review component
def compute_sentiment(review_component, negative_words, positive_words):

    positive = 0
    negative = 0

    for review in review_component:
        if review is None:
            continue
        else:
            words = re.split('\W+', review)
            for word in words:
                if word.lower() in negative_words:
                    negative += 1
                if word.lower() in positive_words:
                    positive += 1
    return {'positive': positive, 'negative': negative}

#evaluates the final sentiment for the product    
def find_sentiment(reviews, sentiment_map):
    
    negative_words = sentiment_map['negative']
    positive_words = sentiment_map['positive']
    review_head = reviews['review_head']
    review_content = reviews['review_content']

    head_value = compute_sentiment(review_head, negative_words, positive_words)
    comment_value = compute_sentiment(review_content, negative_words, positive_words)
    positive = head_value['positive'] + 0.8 * comment_value['positive']
    negative = head_value['negative'] + 0.8 * comment_value['negative']

    if math.fabs(positive - negative) <= 2.5:
        return "debatable"
    elif positive < negative:
        return "negative"
    else:
        return "positive"

#main function, calls all other functions and checks if input is valid
if __name__ == '__main__':

    url = raw_input("\nEnter product url to get sentimental analysis based on recent reviews\n")
    if not url:
        print "You did not enter a url! Exiting...."
        sys.exit()
    
    try:
        html_doc = urllib2.urlopen(url)
        soup = bs(html_doc.read(), 'html.parser')
        reviews = extract_reviews(soup)
        rating = extract_rating(soup)
        print
        print "Overall rating is " + str(rating) 

        if len(reviews['review_head']) != 0:
            sentiment_map = get_sentiment_list()          
            print "Recent reviews are largely " + find_sentiment(reviews, sentiment_map) + " in sentiment"
            print
        else:
            print "Either this product has no reviews or this is not a valid product page"

    except:
        print "Unknown/Incorrect url! Please try with a different one"
        sys.exit()
