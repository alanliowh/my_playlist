# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

from git import Repo

import m3u8

def get_m3u8(url_link):
    # Enable Performance Logging of Chrome.
	desired_capabilities = DesiredCapabilities.CHROME
	desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

	# Create the webdriver object and pass the arguments
	options = webdriver.ChromeOptions()

	# Chrome will start in Headless mode
	options.add_argument('headless')

	# Ignores any certificate errors if there is any
	options.add_argument("--ignore-certificate-errors")

	# Startup the chrome webdriver with executable path and
	# pass the chrome options and desired capabilities as
	# parameters.
	driver = webdriver.Chrome(executable_path="chromedriver.exe",
							chrome_options=options,
							desired_capabilities=desired_capabilities)

	# Send a request to the website and let it load
	driver.get(url_link)

	# Sleeps for 10 seconds
	time.sleep(10)

	# Gets all the logs from performance in Chrome
	logs = driver.get_log("performance")

	# Opens a writable JSON file and writes the logs in it
	with open("network_log.json", "w", encoding="utf-8") as f:
		f.write("[")

		# Iterates every logs and parses it using JSON
		for log in logs:
			network_log = json.loads(log["message"])["message"]

			# Checks if the current 'method' key has any
			# Network related value.
			if("Network.response" in network_log["method"]
					or "Network.request" in network_log["method"]
					or "Network.webSocket" in network_log["method"]):

				# Writes the network log to a JSON file by
				# converting the dictionary to a JSON string
				# using json.dumps().
				f.write(json.dumps(network_log)+",")
		f.write("{}]")

	print("Quitting Selenium WebDriver")
	driver.quit()

	# Read the JSON File and parse it using
	# json.loads() to find the urls containing images.
	json_file_path = "network_log.json"
	with open(json_file_path, "r", encoding="utf-8") as f:
		logs = json.loads(f.read())

	# Iterate the logs
	for log in logs:

		# Except block will be accessed if any of the
		# following keys are missing.
		try:
			# URL is present inside the following keys
			url = log["params"]["request"]["url"]

			# Checks if the extension is .png or .jpg
			if url[len(url)-4:] == "m3u8":
				print(url, end='\n\n')
				url_got_it = url
		except Exception as e:
			pass
	return url_got_it

    # git repo
PATH_OF_GIT_REPO = r'https://github.com/alanliowh/my_playlist.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')     

# Main Function
if __name__ == "__main__":
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=1"
    url = get_m3u8(website)
    
    

	


