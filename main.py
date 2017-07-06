import json
import os
import psycopg2
from urllib import parse

def connectToDB():
	parse.uses_netloc.append("postgres")
	url = parse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname,port=url.port)

def getDefaultOutput():
	reply = {}
	# reply['pgURL'] = os.environ["DATABASE_URL"]
	reply['status'] = 'ok'
	return json.dumps(reply, sort_keys=True, indent=4)

def login():
	reply = {}
	reply['status'] = 'ok'
	reply['method'] = 'login'
	return json.dumps(reply, sort_keys=True, indent=4)

def spin():
	reply = {}
	reply['status'] = 'ok'
	reply['method'] = 'spin'
	return json.dumps(reply, sort_keys=True, indent=4)

def application(environ, start_response):
	status = '200 OK'
	path = environ['PATH_INFO']
	
	if (path == '/login'):
		output = login()
	elif (path == '/spin')
		output = spin()   
	else 
		output = getDefaultOutput()

	# connectToDB()

	#output += json.dumps(environ)

	response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [bytes(output, 'utf-8')]

	# можно использовать [data.encode('utf-8')]. 
	# также The specs says that you can return an itterator here. So either ["OK"] or yield "OK" :)