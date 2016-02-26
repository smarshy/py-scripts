import urllib2
import json 
import sys

#sample values : 
#country code - va , zipcode - 00120
#country code - us , zipcode - 90210
#country code - in , zipcode - 400021

if __name__ == '__main__':

	ccode = raw_input("\nEnter your country code\n")
	zip_code = raw_input("\nEnter your zip code\n")

	if not ccode or not zip_code:
		print "You did not enter a value! Exiting...."
		sys.exit()

	url = "http://api.zippopotam.us/" + str(ccode).lower() + "/" + str(zip_code) 

	try:
		content = json.load(urllib2.urlopen(url))
		if content:
			print "\nYou may be around "
			places = content['places']
			for place in places:
				print place['place name'] + ", " + place['state'] + ", " + content['country']
		print
	except:
		print "\nPlease enter valid values. The database might be missing. Visit API to see supported countries"
		print

