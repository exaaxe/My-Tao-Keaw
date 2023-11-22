from selenium import webdriver
import time 

# Set up the browser
browser = webdriver.Chrome()

# Open YouTube
browser.get("https://www.youtube.com/")

# Search for "Red Sun in the Sky"
search_box = browser.find_element_by_name("search_query")
search_box.send_keys("Red Sun in the Sky")
search_box.submit()

# Click on the first video in the search results
video = browser.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
video.click()


