# Stock Portfolio app using Python and Flask

I would be capturing some key notes while I develop alongside the lessons.

## Part 1: Getting Started

## Setting up the Flask Environment

### Virtual Environment
`$ python3 -m venv venv`
`$ source venv/bin/activate`

### Saving the requirements
It's a good idea to save the packages (including version numbers) that are being used in the project:
`$ pip freeze > requirements.txt`

### Accessing the App on Development Server

When the app is run at first using the Development Server it needs to be accessed at http://127.0.0.1:5000/ in the browser.
Since am developing on a remote linux server and am trying to access the localhost via a browser on the home laptop
The need is to map the port 5000. We use socat.

socat tcp-listen:81,reuseaddr,fork tcp:localhost:5000 &
http://server-ip:81/

### Running the app using the command
`$ flask --app app --debug run`

## Routing
You should now have three routes:

/: without a trailing slash
/about: without a trailing slash
/stocks/: with a trailing slash
Test each route in the browser:

http://127.0.0.1:5000/
http://127.0.0.1:5000/about
http://127.0.0.1:5000/stocks/
It's worth noting that Flask will redirect 'http://127.0.0.1:5000/stocks' (without a slash) to 'http://127.0.0.1:5000/stocks/' (with a slash). However, if you attempt to access 'http://127.0.0.1:5000/about/', a 404 (Not Found) error will be returned as there's technically no function mapped to this URL.

Should you use a trailing slash or not?

By convention, a trailing slash at the end of a URL indicates that the URL is a folder or a directory. In other words, when the list of stocks in a user's portfolio is displayed, the /stocks/ route will be used. This approach indicates that you have routes for individual stocks, like /stocks/1, /stocks/2, /stocks/57, and so forth.

Think of it like a filesystem:
Use a trailing slash when accessing a folder in the file system: cd /data/users/
Leave off the trailing slash when accessing a file: cat /data/users/id.txt

