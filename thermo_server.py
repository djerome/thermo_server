#!local/bin/python

import os
import time
import json
import requests
from flask import Flask, request, abort

app = Flask(__name__)

#initializations
outfile = '/home/pi/thermo/samples'

def append_record(record):
	with open(outfile, 'a') as f:
		json.dump(record, f)
		f.write('\n')
	f.close()

# Function that handles POST for receiving temperature sensor data
@app.route("/thermo/api/temp", methods=['POST'])
def get_temp_event():
	try:
		if request.headers['Content-Type'] == 'application/json':

			# retrieve data from JSON
			temp_data = request.json
			print "Request data = " + str(temp_data)
			append_record(temp_data)
			return "OK", 200
		else:
			return "Unsupported Media Type", 415
	except:
		abort(503)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True, use_reloader=False)
