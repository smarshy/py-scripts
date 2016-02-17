import sys
import urllib2
import json 

#sample usage : python movie_search.py batman 2
#sample usage : python movie_search.py batman 
#First argument is search keyword and second is page number

#gets arguments from terminal
def get_arguments():
	if len(sys.argv) is 3:
		return {'keyword': sys.argv[1], 'page': sys.argv[2]}
	elif len(sys.argv) is 2:
		return {'keyword': sys.argv[1], 'page': 0}
	else:
		print 'No argument given!'
		sys.exit()

#gets url depending on arguments
def get_url():
	args = get_arguments()
	if args['page']:
		url = "http://www.omdbapi.com/?s=" + str(args['keyword']) + "&page=" + str(args['page'])
	else:
		url = "http://www.omdbapi.com/?s=" + str(args['keyword'])
	return url

#displays resultant data
def display_data(results) :
	print "Returned search resuts are: (in the format - movie name, imdb id, type, year )\n"
	for result in results:
		print result['Title'] + "\t" + result['imdbID'] + "\t" + result['Year'] + "\t" + result['Type']

#main function
if __name__ == '__main__':

	url = get_url()
	data = json.load(urllib2.urlopen(url))

	if data['Response']:
		print "\nDisplaying " + str(len(data['Search'])) + " of total " + str(data['totalResults']) +" results \n"
		display_data(data['Search']) 
	else:
		print "Sorry. This page is not available"

	


