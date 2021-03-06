# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

from git import Repo

def get_m3u8(url_link):
    # Enable Performance Logging of Chrome.
	#desired_capabilities = DesiredCapabilities.CHROME
	#desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

	# Create the webdriver object and pass the arguments
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-gpu")
    #browser = webdriver.Chrome(options=chrome_options)

	# Chrome will start in Headless mode
	#chrome_options.add_argument('headless')

	# Ignores any certificate errors if there is any
	#chrome_options.add_argument("--ignore-certificate-errors")

	# Startup the chrome webdriver with executable path and
	# pass the chrome options and desired capabilities as
	# parameters.
	driver = webdriver.Chrome(options=chrome_options )

	# Send a request to the website and let it load
	driver.get(url_link)

	# Sleeps for 10 seconds
	time.sleep(3)

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
				#print(url, end='\n\n')
				url_got_it = url
		except Exception as e:
			pass
	return url_got_it

    # git repo
PATH_OF_GIT_REPO = r'C:\Users\wali\Downloads\my_playlist'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add('auto_list.m3u8','update_m3u8_list.py')
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')     

# Main Function
if __name__ == "__main__":
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    
    lines = []
    ch_name = []
    
    # first
    ch_name.append('tvg-logo="http://news.now.com/revamp2014/images/news_logo_400.png",NOW?????????')
    website = "https://news.now.com/home/live"
    url = get_m3u8(website)
    #url='https://ewcdnsite02.nowe.com/session/09-7788cfa2083c511441a2e6c212c3d/Content/HLS/LIVE/Channel(HLS_CH332N)/index.m3u8'
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/thumb/1/16/Phoenix_InfoNews.svg/1200px-Phoenix_InfoNews.svg.png",?????????????????????')
    url = 'http://playtv-live.ifeng.com/live/06OLEEWQKN4.m3u8'
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/thumb/3/34/Phoenix_Chinese.svg/1200px-Phoenix_Chinese.svg.png",??????????????????')
    url = 'https://playtv-live.ifeng.com/live/06OLEGEGM4G.m3u8'
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://cdn.tdm.com.mo/uploads/attachment/2021-03/a8fbac1841a5372178278304967c69fb.png_w250",????????????')
    url = 'https://live4.tdm.com.mo/ch1/ch1.live/playlist.m3u8'
    lines.append(url)
        
    # channel
    ch_name.append('tvg-logo="https://cdn.tdm.com.mo/uploads/attachment/2021-03/5bde9db9db093ab310ceef6976cd0ee2.png_w250",????????????')
    url = 'https://live4.tdm.com.mo/ch5/info_ch5.live/playlist.m3u8'
    lines.append(url)
    

    
    
    # first
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/6/65/CCTV-1_Logo.png",CCTV1????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=1"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(' tvg-logo="https://upload.wikimedia.org/wikipedia/zh/3/33/CCTV-5_Logo.png",CCTV5????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=5"
    url = get_m3u8(website)
    lines.append(url)
   
    
    
    # channel
    ch_name.append(',CCTV5+??????????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=6"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/0/0c/CCTV-6_Logo.png",CCTV6????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=7"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/4/49/CCTV-8_Logo.png",CCTV8???????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=9"
    url = get_m3u8(website)
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/0/0b/CCTV-13_Logo.png",CCTV13????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=14"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(',CCTV14????????????')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=15"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(',????????????')
    url = 'http://live1.wuhubtv.com/channel2/playlist.m3u8'
    lines.append(url)
        
    # channel
    ch_name.append(',????????????')
    url = 'http://live1.wuhubtv.com/channel1/playlist.m3u'
    lines.append(url)
    
    # write m3u8
    with open('auto_list.m3u8', 'w',encoding="utf-8") as f:
        f.write('#EXTM3U')
        f.write('\n')
        for i in range(0,len(lines)):
            f.write('#EXTINF:1 '+ch_name[i])
            f.write('\n')
            f.write(lines[i])
            f.write('\n')
    
    print('m3u8 file is built successfully ...')
    git_push()
    print('git push done!')
    
    

	


