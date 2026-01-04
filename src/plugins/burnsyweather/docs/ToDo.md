# To Do

[ ] Decide whether to use MetOffice's location or OpenSteetMap's location
    * If OpenStreetMap, rewire self.get_city_from_coords(lat, long) into the flow in burnsyweather.py, and delete the line in the Hours Adaptor : `global_spot_location_hours["location_of_forecast"] = location_name`
    * If MetOffice, delete `self.get_city_from_coords(lat, long)` from burnsyweather, and its commented out references.
    
[] Confirm whether we need the extra info for the `"parameters": [` part of the GlobalSpot resposes - see [hourly](./SampleDataResponses/hourly.json), [daily](./SampleDataResponses/daily.json). If not, delete related commented code in the models - [hourly](./../Models/MetOffice/SiteSpecificHourly.py), [daily](./../Models/MetOffice/SiteSpecificDaily.py)