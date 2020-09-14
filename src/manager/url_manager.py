import requests
import asyncio
import _thread
import time
import sys, bs4, requests, smtplib

def fetchUrls(searchDict):
    url = "http://sandiego.craigslist.org/search/cto?sort=date&max_price=" + str(searchDict["max_price"]) + "&min_price=" + str(searchDict["min_price"]) + "&query=" + searchDict["keywords"]
    
    location = "sandiego"  
    craigslistSite = requests.get(url)
    search = bs4.BeautifulSoup(craigslistSite.text, 'html.parser')
    potentialCars = search.find_all("a")
    API_ROUTE = "http://127.0.0.1:5000/Url"

    for i in range (0, len(potentialCars)):
        textFormat = str(potentialCars[i])
        if( 
                "data-id=" in textFormat
                and location in textFormat
        ):
                beginningIndex = textFormat.find("href=") + 6
                endingIndex = textFormat.find(".html") + 5
                hyperlink = textFormat[beginningIndex: endingIndex]
                params = {'hyperlink': hyperlink, 'keywords': searchDict['id']}
                r = requests.post(url = API_ROUTE, params = params)
                if(r.status_code == 400):
                    break
    
def main():

    while(True):
        API_ROUTE = "http://127.0.0.1:5000/Search"

        r = requests.get(url = API_ROUTE)
        searchArr = r.json()["searches"]
        
        for i in range (0, len(searchArr)):
            _thread.start_new_thread(fetchUrls, (searchArr[i], ))
             


        time.sleep(1000)




if __name__ == "__main__":
    asyncio.run(main())
