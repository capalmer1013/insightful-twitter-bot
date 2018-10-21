import os
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SCROLL_PAUSE_TIME = 5
URL_REPLACE = re.compile("(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S")
# Leave in #
REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\<)|(\>)|(\|)|(\=)|(\+)|(\*)|(\&)|(\^)|(\%)|(\$)|(\`)|(\~)|(\{)|(\})|(@[A-Za-z0-9_-]+)|(via)")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|(\n)|(\s+)")

def crawl_url(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)

    # 20 tweets per scroll
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    count = 0

    while count < 1000:
        print("Getting tweets. Count: ", count, "\n")
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        count += 1

    # Get all tweets
    selector = 'ol#stream-items-id > li.stream-item > .tweet:not(.tweet-has-context) > .content > .js-tweet-text-container > p.tweet-text'
    all_tweet_elements = driver.find_elements_by_css_selector(selector)

    # Clean tweets
    print("Cleaning tweets")
    tweets = [x.text.strip() for x in all_tweet_elements]
    tweets = [URL_REPLACE.sub("", x.lower()) for x in tweets]
    tweets = [REPLACE_WITH_SPACE.sub(" ", x.lower()) for x in tweets]
    tweets = [REPLACE_NO_SPACE.sub("", x.lower()) for x in tweets]

    # Output to file
    with open("outfile1.txt", "w") as outfile:
        print("Writing to file")
        for tweet in tweets:
            outfile.write("%s\n" % tweet)

    driver.quit()
    print("Done")

if __name__=='__main__':
    url = "https://twitter.com/" + os.environ['TWITTER_USERNAME']
    crawl_url(url)