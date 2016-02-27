import requests
import sys
from collections import defaultdict

#getting url response using requests API
def get_responses(url):

	r = requests.get(url)
	response = r.json()
	return response['items']

#main function
if __name__ == '__main__':

	languages = []
	username = raw_input("\nEnter github username\n")
	url = "https://api.github.com/search/repositories?q=fork:false+user:" + username 

	try:
		repos = get_responses(url)
	except:
		print "Check if username is valid/internet connection"
		sys.exit()

	print "\nRepositories vs Language analysis for user " + str(username)
	print

	for repo in repos:
		if repo['language']:
			languages.append(repo['language'])

	analysed = defaultdict(int)

	for language in languages:
		analysed[language] += 1

	for language,value in analysed.items():
		print language + " : " + str(value)
	print





	










	



