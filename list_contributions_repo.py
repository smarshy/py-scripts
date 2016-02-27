import requests
import sys

#getting url response using requests API
def get_responses(url):

	r = requests.get(url)
	response = r.json()
	return response['items']

#main function
if __name__ == '__main__':

	username = raw_input("\nEnter github username\n")
	org = raw_input("\nEnter organization or owner\n")
	repo = raw_input("\nEnter repository\n")
	url = "https://api.github.com/search/issues?q=repo:" + org + "/" + repo + "+author:" + username + "+type:"

	url1 = url + "issue"
	url2 = url + "pr"

	try:
		issues = get_responses(url1)
		prs = get_responses(url2)
	except:
		print "Check if entered details are valid/internet connectivity"
		sys.exit()

	print "\nContributions for user " + str(username) + " for repository " + org + "/" + repo
	print "\nPull requests:\n"

	for pr in prs:
		print pr['html_url']
	print

	print "\nIssues:\n"

	for issue in issues:
		print issue['html_url']
	print

	










	



