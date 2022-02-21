#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

from git import Repo

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
	driver = webdriver.Chrome(executable_path="/Users/agatha/Desktop/my_playlist/chromedriver",
							chrome_options=options,
							desired_capabilities=desired_capabilities)

	# Send a request to the website and let it load
	driver.get(url_link)

	# Sleeps for 10 seconds
	time.sleep(1)

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
PATH_OF_GIT_REPO = r'/Users/agatha/Desktop/my_playlist'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script_mac'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add('auto_list.m3u8','update_m3u8_list_mac.command')
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
    ch_name.append(',TVB翡翠台')
    website = "https://m.iptv222.com/?act=play&token=a40286099238bad221b653fc8b2e9b06&tid=gt&id=1"
    url = get_m3u8(website)
    lines.append(url)

    ch_name.append('tvg-logo="https://seomarketing.hk/wp-content/uploads/2018/08/TVB-inews-300x124.jpg",TVB新聞台')
    website = "https://m.iptv222.com/?act=play&token=6b7212f5e6acbaba49c8e06fe61ed957&tid=gt&id=9"
    url = get_m3u8(website)
    lines.append(url)

    ch_name.append('tvg-logo="https://seomarketing.hk/wp-content/uploads/2018/08/TVB-inews-300x124.jpg",無綫新聞台 2')
    url='http://livetv.dnsfor.me:80/channel.10.m3u8'
    lines.append(url)
    
    ch_name.append('tvg-logo="http://img.tvb.com/corporate/_fck_/image/TVB_Finance%20&%20Information%20logo_2018(1).jpg",TVB无线财经资讯台')
    website = "https://m.iptv222.com/?act=play&token=b62dbc8267237a664a1691d72b380f47&tid=gt&id=10"
    url = get_m3u8(website)
    lines.append(url)

    # first
    ch_name.append('tvg-logo="http://img.tvb.com/corporate/_fck_/image/TVB_Finance%20&%20Information%20logo_2018(1).jpg",無綫財經·資訊台 2')
    url='http://livetv.dnsfor.me:80/channel.11.m3u8'
    lines.append(url)


    ch_name.append(',TVB J2台')
    website = "https://m.iptv222.com/?act=play&token=03c202230cbf78f91bee0f8f2d93d7d9&tid=gt&id=12"
    url = get_m3u8(website)
    lines.append(url)

    ch_name.append(',香港有线新闻台')
    website = "https://m.iptv222.com/?act=play&token=f580372fcd4388d470a93c98d8cf7904&tid=gt&id=24"
    url = get_m3u8(website)
    lines.append(url)


    # first
    ch_name.append('tvg-logo="http://news.now.com/revamp2014/images/news_logo_400.png",NOW新闻台')
    website = "https://m.iptv222.com/?act=play&token=47fd161d4829fa19e175133e550cd535&tid=gt&id=16"
    url = get_m3u8(website)
    lines.append(url)

    # first
    ch_name.append('tvg-logo="http://news.now.com/revamp2014/images/news_logo_400.png",NOW新闻台 2')
    url='http://livetv.dnsfor.me:80/channel.4.m3u8'
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/thumb/1/16/Phoenix_InfoNews.svg/1200px-Phoenix_InfoNews.svg.png",凤凰卫视资讯台')
    url = 'http://playtv-live.ifeng.com/live/06OLEEWQKN4.m3u8'
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/thumb/3/34/Phoenix_Chinese.svg/1200px-Phoenix_Chinese.svg.png",凤凰卫视中文')
    url = 'https://playtv-live.ifeng.com/live/06OLEGEGM4G.m3u8'
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://cdn.tdm.com.mo/uploads/attachment/2021-03/a8fbac1841a5372178278304967c69fb.png_w250",澳視澳門')
    url = 'https://live4.tdm.com.mo/ch1/ch1.live/playlist.m3u8'
    lines.append(url)
        
    # channel
    ch_name.append('tvg-logo="https://cdn.tdm.com.mo/uploads/attachment/2021-03/5bde9db9db093ab310ceef6976cd0ee2.png_w250",澳视资讯')
    url = 'https://live4.tdm.com.mo/ch5/info_ch5.live/playlist.m3u8'
    lines.append(url)
    

    
    
    # first
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/6/65/CCTV-1_Logo.png",CCTV1综合高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=1"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(' tvg-logo="https://upload.wikimedia.org/wikipedia/zh/3/33/CCTV-5_Logo.png",CCTV5体育高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=5"
    url = get_m3u8(website)
    lines.append(url)
   
    
    
    # channel
    ch_name.append(',CCTV5+体育赛事高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=6"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/0/0c/CCTV-6_Logo.png",CCTV6电影高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=7"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/4/49/CCTV-8_Logo.png",CCTV8电视剧高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=9"
    url = get_m3u8(website)
    lines.append(url)
    
    
    # channel
    ch_name.append('tvg-logo="https://upload.wikimedia.org/wikipedia/zh/0/0b/CCTV-13_Logo.png",CCTV13新闻高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=14"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(',CCTV14少儿高清')
    website = "https://m.iptv222.com/?act=play&token=420dde623e40d4de45c6133c725e470e&tid=ys&id=15"
    url = get_m3u8(website)
    lines.append(url)
    
    # channel
    ch_name.append(',芜湖生活')
    url = 'http://live1.wuhubtv.com/channel2/playlist.m3u8'
    lines.append(url)
        
    # channel
    ch_name.append(',芜湖新聞')
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
    
    

	


