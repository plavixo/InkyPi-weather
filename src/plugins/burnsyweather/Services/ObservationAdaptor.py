import os
import requests
import json

from plugins.burnsyweather.Models.MetOffice.Observations import ObservationsRoot, list_from_json

class ObservationAdaptor:
    base_url = "https://data.hub.api.metoffice.gov.uk/observation-land/1"
    def get_observation_params(self,latitude, longitude):
        geohash=self.retrieve_cached_geohash(latitude, longitude)
        print ("Geohash: ", geohash)

        rawObservationData = self.get_observations(geohash)

        # Write to file for debugging
        f = open("observations", "w")
        f.write(rawObservationData)
        print("File created: ", os.path.abspath(f.name))
        f.close()  

        params = {}

        
        # jsonstring = json.loads(rawObservationData)
        # observations = list_from_json(jsonstring)

        # latest_entry = observations[-1]

        #     'observation_datetime': latest_entry.datetime,
        #     'observation_humidity': latest_entry.humidity,
        #     'observation_mslp': latest_entry.mslp,
        #     'observation_pressure_tendency': latest_entry.pressure_tendency,
        #     'observation_temperature': latest_entry.temperature,
        #     'observation_visibility': latest_entry.visibility,
        #     'observation_weather_code': latest_entry.weather_code,
        #     'observation_wind_direction': latest_entry.wind_direction,
        #     'observation_wind_gust': latest_entry.wind_gust,
        #     'observation_wind_speed': latest_entry.wind_speed
        # }




        return params

    def get_observations(self, geohash):
        endpoint = f"/{geohash}"
        params = {}

        rawObservations = self.make_request(endpoint, params)
        print("Raw Observations: ", rawObservations)
        return rawObservations
    

    def retrieve_cached_geohash(self, latitude, longitude):
        return "gcnfur"
    
    def retrieve_geohash(self, latitude, longitude):

        truncated_latitude = f"{latitude:.2f}"
        truncated_longitude = f"{longitude:.2f}"
        params = {
            'lat' : truncated_latitude,
            'lon' : truncated_longitude
        }

        endpoint = "/nearest"

        rawGeohash = self.make_request(endpoint, params)
        jsonstring = json.loads(rawGeohash)
        geohash = jsonstring[0]['geohash']
        return geohash

    def make_request(self, endpoint, params):
    
        url = self.base_url + endpoint
        
        api_key = self.get_secret("MetOffice", "ObservationsAPIKey")
        
        requestHeaders = {"apikey": api_key}
        headers = {'accept': "application/json"}
        headers.update(requestHeaders)
        

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