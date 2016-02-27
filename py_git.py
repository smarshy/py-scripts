import requests
import sys

def get_responses(url):

	r = requests.get(url)
	response = r.json()
	return response['total_count']

if __name__ == '__main__':

	statistics = {}
	username = raw_input("\nEnter github username\n")
	url = "https://api.github.com/search/issues?q=author:" + username + "+type:"

	url1 = url + "issue"
	url2 = url + "issue+is:closed"
	url3 = url + "issue+is:open"
	url4 = url + "pr"
	url5 = url + "pr+is:open"
	url6 = url + "pr+is:closed+is:unmerged"
	url7 = url + "pr+is:closed+is:merged"

	try:
		statistics['Total Issues'] = get_responses(url1)
		statistics['Closed Issues'] = get_responses(url2)
		statistics['Open Issues'] = get_responses(url3)
		statistics['Open PRs'] = get_responses(url5)
		statistics['Unmerged PRs'] = get_responses(url6)
		statistics['Merged PRs'] = get_responses(url7)
		statistics['Total PRs'] = get_responses(url4)
	except:
		print "Check if username is valid/internet connection"
		sys.exit()

	print
	print "Statistics for user " + str(username)
	print

	for key,value in statistics.items():
		print str(key) + " : " + str(value)
	print










	



