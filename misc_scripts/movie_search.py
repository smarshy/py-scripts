import sys
import urllib2
import json 

def get_arguments():
	if len(sys.argv) is 3:
		return {'keyword': sys.argv[1], 'page': sys.argv[2]}
	elif len(sys.argv) is 2:
		return {'keyword': sys.argv[1], 'page': 0}
	else:
		print 'No argument given!'
		sys.exit()

def get_url():
	args = get_arguments()
	if args['page']:
		url = "http://www.omdbapi.com/?s=" + str(args['keyword']) + "&page=" + str(args['page'])
	else:
		url = "http://www.omdbapi.com/?s=" + str(args['keyword'])
	return url

def display_data(results) :
	print "Returned search resuts are: (in the format - movie name, imdb id, type, year )"
	for result in results:
		print result['Title'] + "\t" + result['imdbID'] + "\t" + result['Year'] + "\t" + result['Type']

if __name__ == '__main__':

	url = get_url()
	data = json.load(urllib2.urlopen(url))

	if data['Response']:
		print "Displaying" + str(len(data['Search'])) + " of total " + str(data['totalResults']) +" results "
		display_data(data['Search']) 
	else:
		print "Sorry. This page is not available"

	


