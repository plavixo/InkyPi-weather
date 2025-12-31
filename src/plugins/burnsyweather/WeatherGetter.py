import os
import sys
from urllib.request import urlopen
import json
import time
import requests
from plugins.burnsyweather.Models.MetOffice.SiteSpecific import *

class WeatherGetter:
    base_url = "https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/"


    def get_content(self):
     
        # url = "http://olympus.realpython.org/profiles/aphrodite"
        # page = urlopen(url)
        # html_bytes = page.read()
        # html = html_bytes.decode("utf-8")
        # title_index = html.find("<title>")
        # start_index = title_index + len("<title>")
        # end_index = html.find("</title>")
        # title = html[start_index:end_index]

        # print(f"Title of the page is: {title}")

        print(self.base_url)

        api_key = self.get_value_from_json("MetOffice", "APIKey")
        print(api_key[:10])


        timesteps = "hourly"
        includeLocation = "TRUE"
        excludeMetadata = "FALSE"
        latitude = "-3.474"
        longitude = "50.727"
 

        requestHeaders = {"apikey": api_key}
        outcome = self.retrieve_forecast(self.base_url, timesteps, requestHeaders, latitude, longitude, excludeMetadata, includeLocation)

        jsonstring = json.loads(outcome)
        root = Root.from_dict(jsonstring)

        print(f"Root.type: {root.type}")



        return f"It's going to be a superb day"
    
    def get_value_from_json(self, key, sub_key):

        print("Getting value from JSON")

        json_file=os.path.join(os.getenv('APPDATA'), "Python\\Secrets\\InkyPi-Weather\\secrets.json")

        try:
            with open(json_file) as f:
                data = json.load(f)
                thing = data[key][sub_key]
                print("Found value:")
                return thing
        except Exception as e:
            print("Error Getting Secrets: ", e)

    def retrieve_forecast(self,baseUrl, timesteps, requestHeaders, latitude, longitude, excludeMetadata, includeLocation):
    
        url = baseUrl + timesteps 
        
        headers = {'accept': "application/json"}
        headers.update(requestHeaders)
        params = {
            'excludeParameterMetadata' : excludeMetadata,
            'includeLocationName' : includeLocation,
            'latitude' : latitude,
            'longitude' : longitude
            }

        success = False
        retries = 5

        while not success and retries >0:
            try:
                req = requests.get(url, headers=headers, params=params)
                success = True
            except Exception as e:
                print("Exception occurred", exc_info=True)
                retries -= 1
                time.sleep(10)
                if retries == 0:
                    print("Retries exceeded", exc_info=True)
                    sys.exit()

        req.encoding = 'utf-8'

        print(req.text)

        return req.text
