import string
import re
from collections import Counter

import wikipedia

STOPWORD_FILE = "/home/vatsala/py-scripts/misc_scripts/wiki_count/stopwords.txt"

#Loads and returns words from a custom stopword text file
def get_stopWord_list():
	inFile = open(STOPWORD_FILE, 'r', 0)
	line = inFile.readline()
	stopwordlist = string.split(line)
	inFile.close()
	return stopwordlist

#Returns list of all words in the content, excluding the stop words 
def get_contentWord_list(content, stopwordlist):
	contentwordlist = re.split('\W+', content)
	consolidatedlist = [word for word in contentwordlist if word not in stopwordlist]
	return consolidatedlist

#Returns a sorted list of 10 most common words with their frequency
def get_word_frequency(contentwordlist):
	return Counter(contentwordlist).most_common(10)

#Displays content analysis details for the page
def display_content_analysis(details, wordfreq):
	print "\nPage Details:\n"
	for key, value in details.iteritems(): 
		print str(key) + " : " + str(value)
	print "\nThe following are the ten most common words on the page along with their frequencies:\n"	
	for key,value in wordfreq:
		print str(key) + " - " + str(value)

def main():
	try:
		wikipedia.set_lang("en")
		page_name = raw_input("Enter a wikipedia page to analyse\n")
		page = wikipedia.page(page_name)
		details = {'Topic' : page.title, 'Url' : page.url, 'Number of links on the page' : len(page.links)}
		stopwordlist = get_stopWord_list()
		stopwordlist.extend(re.split('\W+', str(page.title).lower()))
		contentwordlist = get_contentWord_list(page.content.encode('utf-8').lower(), stopwordlist)
		wordfreq = get_word_frequency(contentwordlist)
		display_content_analysis(details, wordfreq)
	except:
		print "Invalid page entered or no internet connection"

#Calls main function
if __name__ == '__main__':
	main()