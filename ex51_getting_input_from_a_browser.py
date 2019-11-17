# Getting Input from a Browser
# directory: gothonweb

""" Browser The software that you’re probably using every day. Most people don’t know what a browser
really does. They just call browsers ”the internet.” Its job is to take addresses (like http://test.com/)
you type into the URL bar, then use that information to make requests to the server at that address.

Address This is normally a URL (Uniform Resource Locator) like http://test.com// and indicates where a
browser should go. The first part, http, indicates the protocol you want to use, in this case ”Hyper-
Text Transport Protocol.” You can also try ftp://ibiblio.org/ to see how ”File Transport Protocol”
works. The http://test.com/ part is the ”hostname,” a human readable address you can remember
and which maps to a number called an IP address, similar to a telephone number for a computer on
the internet. Finally, URLs can have a trailing path like the /book/ part of http://test.com//book/,
which indicates a file or some resource on the server to retrieve with a request. There are many
other parts, but those are the main ones.

Connection Once a browser knows what protocol you want to use (http), what server you want to talk
to (http://test.com/), and what resource on that server to get, it must make a connection. The
browser simply asks your operating system (OS) to open a ”port” to the computer, usually port
80. When it works, the OS hands back to your program something that works like a file, but is
actually sending and receiving bytes over the network wires between your computer and the other
computer at http://test.com/. This is also the same thing that happens with http://localhost:8080/,
but in this case you’re telling the browser to connect to your own computer (localhost) and use
port 8080 rather than the default of 80. You could also do http://test.com:80/ and get the same
result, except you’re explicitly saying to use port 80 instead of letting it be that by default.

Request Your browser is connected using the address you gave. Now it needs to ask for the resource
it wants (or you want) on the remote server. If you gave /book/ at the end of the URL, then
you want the file (resource) at /book/, and most servers will use the real file /book/index.html
but pretend it doesn’t exist. What the browser does to get this resource is send a request to the
server. I won’t get into exactly how it does this, but just understand that it has to send something
to query the server for the request. The interesting thing is that these ”resources” don’t have
to be files. For instance, when the browser in your application asks for something, the server is
returning something your Python code generated. """