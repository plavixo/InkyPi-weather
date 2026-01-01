Magic code to run things - remember to manually attach the debugger.  
`python -m debugpy --listen localhost:8080 src/inkypi.py --dev`

[Observation Adaptor](./../Services/ObservationAdaptor.py)
* is hardcoded to use the (also hardcoded) cached geohash.
* also uses the secrets file

