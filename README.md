![LightFeather IO alternate logo](https://github.com/BradyHammond/lightfeatherIO_assessment/blob/master/client/static/images/lightfeather_logo_banner.png)

Overview
========
This is an assessment for LightFeather IO LLC. It consists of a simple backend API and a frontend web component. For an 
in depth specification please refer to the Specs.pdf file.

Installation
============
This installation assumes you're using a unix based machine. To install the project first checkout the git repository:
```
$ git clone https://github.com/BradyHammond/lightfeatherIO_assessment.git
```
This project requires Python3 and Node.js. If needed, corresponding installation instructions can be found 
[here](https://www.python.org/downloads/) and [here](https://nodejs.org/en/download/) respectively. To verify that you 
have both downloaded correctly you can run the following commands:
```
$ python3 --version
$ node -v
```
It is recommended that you run this project in a virtual environment. To setup a Python virtual environment download 
virtualenv, navigate to the project repo, and run the following commands:
```
$ pip3 install virtualenv
$ cd lightfeatherIO_assessment
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
Next install the needed python dependencies:
```
$ pip3 install -r requirements.txt
```
That concludes the required backend setup. Now it's time to setup the frontend. Navigate from the project's root
directory to the client folder and download the frontend dependencies using npm:
```
$ cd client
$ npm install
```
The last step is to make a webpack build, so the web server can serve the frontend statically. To do this run the 
following command:
```
$ npm run build
```

Usage
=====
Both parts of the project can be tested at once. For convenience the backend serves the fronted web component. To start
the server navigate to the project's root directory and run:
```
$ python3 app.py
```
This will start the server on the localhost (127.0.0.1) on port 23456. The web component uses the default route 
(http://127.0.0.1:23456). As per the project specs, the API uses the route http://127.0.0.1:23456/api/encode. The web
component has been tested for cross-platform compatibility (excluding IE) and responsiveness, so you should be able to 
test the client on any browser or device. To test the API, you can use curl commands:
```
$ curl -i -X POST -H "Content-Type: application/json" -d '{"Shift":2, "Message":"test"}' http://localhost:23456/api/encode
```
Or you can use a UI interface like the one featured [here](https://insomnia.rest/). The project saves encoded messages 
in the saves folder of the project using a unique ID each time it successfully encodes a message. If for any reason you
receive a 500 error due to the permissions of the saves directory, you can rectify the issue by navigating to the
project's root directory and running the command:
```
$ chmod 777 saves
```
For any further questions on how to test the project, please reach out to me directly.

Teardown
========
When you are finished with the project don't forget to deactivate your virtual environment. You can do so by running 
the following command:
```
$ deactivate
```

Tech Stack
==========
This project uses the Python framework Flask on the backend and the JavaScript framework vue.js on the frontend. This
stack was chosen to keep the project lightweight while allowing for future extensibility. I have used both Python
and JavaScript in the past, but this was my first exposure to vue.js and Flask. In addition to the lightweight benefits
these options provided, I chose these frameworks to highlight my ability to quickly learn and utilize new technologies.
If you have any further questions about my reasonings, please reach out to me directly.
