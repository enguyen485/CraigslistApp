from apscheduler.schedulers.background import BackgroundScheduler
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta
from models.detectors import Detector	
from models.url import Url
import sys, bs4, requests, smtplib
import asyncio
import time

class DetectorManager(Resource):
    __instance = None
    __job_scheduler = BackgroundScheduler()

    def __init__(self):
        DetectorManager.__instance = self
        DetectorManager.__job_scheduler.start()

    @staticmethod
    def getInstance():
        if DetectorManager.__instance == None:
            DetectorManager()
        return DetectorManager.__instance

    def initialize(self):
        detectors = Detector.get_all_detectors()
        for detector in detectors:
            self.addJob(detector, False)

    def addJob(self, detector, is_new):
        url = "http://sandiego.craigslist.org/search/cto?sort=date&max_price="\
              + str(detector.max_price) + "&min_price=" + str(detector.min_price)\
              + "&query=" + detector.keywords
        DetectorManager.__job_scheduler.add_job(self.__runDetector, 'date', 
                                                run_date = self.__getRuntime(), 
                                                args=(detector.id, url, is_new))   

    def __runDetector(self, id, url, is_new): 
        craigslistSite = requests.get(url)
        search = bs4.BeautifulSoup(craigslistSite.text, 'html.parser')
        links = search.find_all("a")
         
        matchFound = False
        for link in links:
            textFormat = str(link)
            if("data-id=" not in textFormat 
               or "sandiego" not in textFormat):
                continue
            matchFound = True
            beginningIndex = textFormat.find("href=") + 6
            endingIndex = textFormat.find(".html") + 5
            hyperlink = textFormat[beginningIndex: endingIndex]
                
            if(is_new == True):
                inputData = {}
                inputData["hyperlink"] = hyperlink
                inputData["keywords"] = id
                inputData["is_deleted"] = False
                if Url.find_url_by_hyperlink(inputData['hyperlink'], inputData['keywords']):
                    return 
                Url(**inputData).save()
                
        if not matchFound:
            DetectorManager.__job_scheduler.add_job(self.__runDetector, 'date', 
                                                    run_date = self.__getRuntime(), 
                                                    args=(id, url, is_new)) 

    def __getRuntime(self):
        return datetime.now() + timedelta(0, 500)
