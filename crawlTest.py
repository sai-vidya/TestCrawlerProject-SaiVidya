import urllib.request
import json
import os
f = open("crawlTestLog.txt", "wb")
s = object
FileToOpen = os.path.abspath('crawlUrls.json')
try:
    with open(FileToOpen) as urlInputs:
        results = json.load(urlInputs)
        for url in results["sites"]["url"]:
            with urllib.request.urlopen(url) as s:
                crawlData = s.read()
                json.dump(crawlData, f)
    f.close()
except Exception:
    print("Error in crawling. Please check crawlTestLog file for more details")
