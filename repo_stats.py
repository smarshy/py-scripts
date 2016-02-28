import requests
import sys
from collections import defaultdict

#getting url response using requests API
def get_response(url):

	r = requests.get(url)
	response = r.json()
	return response

#main function
if __name__ == '__main__':

	repositories = []
	username = raw_input("\nEnter github username\n")
	url = "https://api.github.com/users/" + username  + "/repos" 

	try:
		repos = get_response(url)
	except:
		print "Check if username is valid/internet connection"
		sys.exit()

	print "\nRepositories for user " + str(username)
	print

	for repo in repos:
		if not repo['fork'] and not repo['private']:
			repositories.append(str(repo['full_name']))

	print repositories

	for repo in repositories:
		url_for_repo = "https://api.github.com/repos/" + str(repo) + "/stats/commit_activity" 
		print repo
		try:
			data = get_response(url_for_repo)
			if data:
				recent = [data[-1]['days'], data[-2]['days'], data[-3]['days'], data[-4]['days']]
				print recent
			else:
				print "Slow Internet Connection"
		except:
			print "Error in internet connection"
			sys.exit()
	 







	










	



