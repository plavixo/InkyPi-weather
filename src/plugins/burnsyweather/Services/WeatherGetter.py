import os
import sys
from urllib.request import urlopen
import json
import time
import requests

from plugins.burnsyweather.Services.SecretGetter import SecretGetter


class WeatherGetter:
    base_url = "https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/"


    def get_content(self, lat, long, timesteps):    

        secret_getter = SecretGetter()
        api_key = secret_getter.get_secret("MetOffice", "APIKey")
        print(api_key[:10])


        includeLocation = "TRUE"
        excludeMetadata = "FALSE"
        latitude = lat
        longitude = long
 

        requestHeaders = {"apikey": api_key}
        outcome = self.retrieve_forecast(self.base_url, timesteps, requestHeaders, latitude, longitude, excludeMetadata, includeLocation)

        # Write to file for debugging
        f = open(timesteps, "w")
        f.write(outcome)
        print("File created: ", os.path.abspath(f.name))
        f.close()  


        return outcome
    
    # def get_secret(self, key, sub_key):
    #     # TODO: Change this to get from static file location which will work with the Pi

    #     print("Getting value from JSON")

    #     json_file=os.path.join(os.getenv('APPDATA'), "Python\\Secrets\\InkyPi-Weather\\secrets.json")
    #     if json_file is None or not os.path.exists(json_file):
    #         json_file=os.path.join(os.path.expanduser("~"), ".config/InkyPi-Weather/secrets.json")


    #     try:
    #         with open(json_file) as f:
    #             data = json.load(f)
    #             thing = data[key][sub_key]
    #             print("Found value:")
    #             return thing
    #     except Exception as e:
    #         print("Error Getting Secrets: ", e)

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

        # print(req.text)

        return req.text
