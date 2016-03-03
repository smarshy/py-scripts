import re

import wikipedia

def main():
	try:
		wikipedia.set_lang("en")
		page_name = raw_input("Enter a wikipedia page to analyse\n")
		page = wikipedia.page(page_name)
		details = {'Topic' : page.title, 'Url' : page.url, 'Number of links on the page' : len(page.links)}
		print details
	except:
		print "Invalid page entered or no internet connection"

#Calls main function
if __name__ == '__main__':
	main()