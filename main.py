import json
import os
import psycopg2
import urlparse

def connectToDB():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(
    	database=url.path[1:],
    	user=url.username,
    	password=url.password,
    	host=url.hostname,
    	port=url.port
	)

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n\n'
    
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

