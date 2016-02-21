import sys
import urllib2
import json 

#Example : python rhyming_word.py ajar

#gets arguments from terminal
def get_arguments():

	if len(sys.argv) is 2:
		return sys.argv[1]
	else:
		print 'No argument given!'
		sys.exit()

#gets url depending on arguments
def get_url():

	word = get_arguments()
	url = 'http://api.wordnik.com:80/v4/word.json/' + str(word) + '/relatedWords?useCanonical=false&relationshipTypes=rhyme&limitPerRelationshipType=200&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
	return url

#displays rhyming words for the given word
def display_rhyming_words(result) :

	for word in result['words']:
		print word

	print

#calls other functions
if __name__ == '__main__':

	url = get_url()
	result = json.load(urllib2.urlopen(url))

	if result:
		print "\nRhyming words are :\n"
		display_rhyming_words(result[0])
	else:
		print "Sorry. This page is not available"

	


