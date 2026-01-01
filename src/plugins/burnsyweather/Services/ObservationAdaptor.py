import os
import requests
import json

class ObservationAdaptor:
    base_url = "https://data.hub.api.metoffice.gov.uk/observation-land/1"
    def get_observation_params(self,latitude, longitude):
        geohash=self.retrieve_cachedGeohash(latitude, longitude)
        print ("Geohash: ", geohash)

        return {}
    



    def retrieve_cachedGeohash(self, latitude, longitude):
        return "gcnfur"
    
    def retrieve_geohash(self, latitude, longitude):
        rawGeohash = self.get_rawGeohash(latitude, longitude)
        jsonstring = json.loads(rawGeohash)
        geohash = jsonstring[0]['geohash']
        return geohash

    def get_rawGeohash(self, latitude, longitude):
    
        truncated_latitude = f"{latitude:.2f}"
        truncated_longitude = f"{longitude:.2f}"

        url = self.base_url + "/nearest"
        
        api_key = self.get_secret("MetOffice", "ObservationsAPIKey")
        
        requestHeaders = {"apikey": api_key}
        headers = {'accept': "application/json"}
        headers.update(requestHeaders)
        params = {
            'lat' : truncated_latitude,
            'lon' : truncated_longitude
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
    
    def get_secret(self, key, sub_key):
        # TODO: Change this to get from static file location which will work with the Pi

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