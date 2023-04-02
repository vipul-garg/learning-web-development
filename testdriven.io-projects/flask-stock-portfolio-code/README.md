# Stock Portfolio app using Python and Flask

I would be capturing some key notes while I develop alongside the lessons.

## Part 1: Getting Started
When the app is run at first using the Development Server it needs to be accessed at http://127.0.0.1:5000/ in the browser.
Since am developing on a remote linux server and am trying to access the localhost via a browser on the home laptop
The need is to map the port 5000. We use socat.

socat tcp-listen:81,reuseaddr,fork tcp:localhost:5000 &
http://<server IP>:81/