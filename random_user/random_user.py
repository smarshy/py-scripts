import urllib2
import json 

OUTPUT_FILE = "/home/vatsala/myscripts/random_user/generated.txt"
    
#main function
if __name__ == '__main__':

	url = "https://randomuser.me/api/"
	num = int(raw_input("\nEnter number of random credentials you want to generate\n"))

	outFile = open(OUTPUT_FILE, 'w')

	for entry in range(0,num):
		response = json.load(urllib2.urlopen(url))
		user = response['results'][0]['user']
		username = user['username']
		password = user['password']
		outFile.write("\n")
		outFile.write("### Random User " + str(entry + 1))
		outFile.write("\n")
		outFile.write("Username: " + username)
		outFile.write("\n")
		outFile.write("Password: " + password)
		outFile.write("\n")

	outFile.close()

	
