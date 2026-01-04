import json
import os

class SecretGetter:
     def get_secret(self, key, sub_key):
        print("Getting value from JSON")

        json_file=os.path.join(os.getenv('APPDATA'), "Python\\Secrets\\InkyPi-Weather\\secrets.json")
        if json_file is None or not os.path.exists(json_file):
            json_file=os.path.join(os.path.expanduser("~"), ".config/InkyPi-Weather/secrets.json")

        try:
            with open(json_file) as f:
                data = json.load(f)
                thing = data[key][sub_key]
                print("Found value:")
                return thing
        except Exception as e:
            print("Error Getting Secrets: ", e)