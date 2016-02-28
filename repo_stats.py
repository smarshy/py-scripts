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

	days_count = {}
	days_count['sunday'] = 0
	days_count['monday'] = 0
	days_count['tuesday'] = 0
	days_count['wednesday'] = 0
	days_count['thursday'] = 0
	days_count['friday'] = 0
	days_count['saturday'] = 0

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
			data = get_response(url_for_repo)
			if data:
				recent = [data[-1]['days'], data[-2]['days'], data[-3]['days'], data[-4]['days']]

				for week in recent:
					days_count['sunday'] += week[0]
					days_count['monday'] += week[1]
					days_count['tuesday'] += week[2]
					days_count['wednesday'] += week[3]
					days_count['thursday'] += week[4]
					days_count['friday'] += week[5]
					days_count['saturday'] += week[6]				

			else:
				print "Slow Internet Connection"
		except:
			print "Error in internet connection"
			sys.exit()

	print
	print "Commit activity pattern for user owned repositories in the past month -"
	print

	for key, value in days_count.items():
		print str(key) + " : " + str(value)
	 







	










	



