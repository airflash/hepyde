import json
import os
import psycopg2
from urllib import parse

def connectToDB():
	parse.uses_netloc.append("postgres")
	url = parse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname,port=url.port)

def getOutput():
	reply = {}
	reply['pgURL'] = os.environ["DATABASE_URL"]
	reply['status'] = 'ok'
	replu['path'] = environ['PATH_INFO']
	return json.dumps(reply, sort_keys=True, indent=4)

def application(environ, start_response):
    status = '200 OK'
    output = getOutput()
    # output += "\n"
    

    

    # for keys,values in environ.items():
    # 	output += str(keys) + '\n'
    # 	output += str(values) + '\n'

    connectToDB()

    #output += json.dumps(environ)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [bytes(output, 'utf-8')]
    
    # можно использовать [data.encode('utf-8')]. 
    # также The specs says that you can return an itterator here. So either ["OK"] or yield "OK" :)