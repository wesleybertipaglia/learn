# http
host, port = "localhost", 8080
method, url = 'GET', '/'

# client
import http.client

# Create an HTTP connection to a server
connection = http.client.HTTPConnection(host, port)

# Create an HTTPS connection to a server
connection = http.client.HTTPSConnection(host, port)

# Send an HTTP request
connection.request(method, url, body=None, headers={})

# Get the HTTP response
response = connection.getresponse()


# server
import http.server

# Set up the server address
server_address = ('localhost', 8080) 

# Create an HTTP server with a custom request handler
handler_class = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler_class)

# Start the HTTP server
server.serve_forever()

# cookies
from http import cookies

cookie = cookies.SimpleCookie() # Create a cookie object
cookie['name'] = 'value' # Set a cookie value

# Set additional attributes for the cookie
cookie['name']['path'] = '/path'
cookie['name']['expires'] = 3600  # Expires in 1 hour
cookie['name']['domain'] = 'example.com'
