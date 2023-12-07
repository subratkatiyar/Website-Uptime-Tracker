import requests
import time

def siteListParser():
    fileDescriptor = open("./site_list.txt")
    websiteList = fileDescriptor.read()
    return websiteList.split('\n')

def sitePingUtility(siteName):
    return requests.get(siteName).elapsed.total_seconds()

def readmeUpdater(siteName, timeStamp, responseTime):
    f = open("./readme.md", "a")
    f.write(f'| {siteName} | {time.ctime(timeStamp)} | {responseTime} |\n')
    f.close()

if __name__ == '__main__':
    siteList = siteListParser()
    for site in siteList:
        timeStamp = time.time() 
        responseTime = sitePingUtility(site)
        readmeUpdater(site, timeStamp, responseTime)
     