import json
import os
import sys

class SecretGetter:
     def get_secret(self, key, sub_key):
        print("Getting value from JSON")

        if sys.platform.startswith('win'):
            print("Running on Windows")
            json_file=os.path.join(os.getenv('APPDATA'), "Python\\Secrets\\InkyPi-Weather\\secrets.json")
        elif sys.platform.startswith('linux'):
            print("Running on Linux")
            json_file=os.path.join(os.path.expanduser("~"), ".config/InkyPi-Weather/secrets.json")
        else:
            print("Unsupported platform")

        try:
            with open(json_file) as f:
                data = json.load(f)
                thing = data[key][sub_key]
                print("Found value:")
                return thing
        except Exception as e:
            print("Error Getting Secrets: ", e)