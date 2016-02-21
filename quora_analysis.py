from __future__ import division
import sys

from quora import User
from quora import Activity
from quora import Quora

#Usage sample: python quora_analysis.py Vatsala-Swaroop-1

#gets username argument from terminal
def get_arguments():
	if len(sys.argv) is 2:
		return sys.argv[1]
	else:
		print 'No argument given!'
		sys.exit()

#fetches stats for a user
def get_stats(user):
	return user.stats

#fetches activity for a user
def get_activity(name):
	activity = Quora.get_activity(name)
	data = {'Upvoted Answers':len(activity.upvotes), 'Followed Topics':len(activity.user_follows), 'Want Answers':len(activity.want_answers), 'Review Requests':len(activity.review_requests)}
	return data

#displays statistics for a particular user
def display_stats(stat):
	print "\nUser Stats:\n"
	for key, value in stat.iteritems(): 
		print str(key).title() + " :  " + "\t" + str(value) 

#Analyses and dispays activity usage for a particular user
def display_activity_analysis(data):
	print "\nActivity Analysis:\n"
	total = sum(data.values())

	if total==0:
		print "The user has no other activity"
		return

	for key, value in data.iteritems(): 
		print key + " :   " + "\t" + "{0:.2f}".format(value*100/total)  + "%"
	print "\n"

if __name__ == '__main__':
	name = get_arguments()

	if name:
		user = User(name)
		stats = get_stats(user)
		if not stats:
			print "Requested username is invalid! Please retry..."
			sys.exit()
		display_stats(stats)
		data = get_activity(name)		
		display_activity_analysis(data)
	else:
		print 'You did not specify a username'
    
	

