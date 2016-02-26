import urllib2
import json 

if __name__ == '__main__':

	ccode = "IN"
	zip_code ="440010"
	url = "http://api.zippopotam.us/" + ccode + "/" + zip_code 

	content = json.load(urllib2.urlopen(url))

	if content:
		print "You are located at "
		places = content['places']
		for place in places:
			print place['place name'] + ", " + place['state'] + ", " + content['country']
	else:
		print "Please try again with valid codes. Visit API to see supported countries"