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

	connectToDB()

	#TODO: если юзер есть в базе - вернуть токен сессии
	#TODO: если нет в базе - записать туда его
	
	reply = {}
	reply['status'] = 'ok'
	reply['method'] = 'login'
	return json.dumps(reply, sort_keys=True, indent=4)

def spin():
	reply = {}
	reply['status'] = 'ok'
	reply['method'] = 'spin'
	return json.dumps(reply, sort_keys=True, indent=4)

def route(environ):
	path = environ['PATH_INFO']

	if (path == '/login'):
		return login()
	elif (path == '/spin'):
		return spin()   
	else :
		return getDefaultOutput()

def application(environ, start_response):
	status = '200 OK'
		
	output = route(environ)	

	for keys,values in environ.items():
		output += str(keys) + '\n'
		output += str(values) + '\n'

	response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [bytes(output, 'utf-8')]