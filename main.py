import json

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n'
    output += environ
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [bytes(output, 'utf-8')]
    
    # можно использовать [data.encode('utf-8')]. 
    # также The specs says that you can return an itterator here. So either ["OK"] or yield "OK" :)
