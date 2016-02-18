import urllib2
from bs4 import BeautifulSoup as bs


def extract_reviews(url):
    html_doc = urllib2.urlopen(url)
    soup = bs(html_doc.read(), 'html.parser')
    review_head = [str(review.findAll('p')[0].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    review_content = [str(review.findAll('p')[1].get_text()) for review in soup.findAll('div', class_ ='r-detail')]
    return {'review_head': review_head, 'review_content': review_content}


if __name__ == '__main__':
    url = 'http://www.nykaa.com/bath-and-body/nivea-body-lotion-extra-whitening-cell-repair-uv-protect-vit-c.html?root=catg_Nykaas%20Choice&ptype=product&brand=catg_nykaas+choice'
    reviews = extract_reviews(url)
    print reviews