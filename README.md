# websocket-example
Small example for data exchange over websockets.

See [this blog post](https://www.kleemans.ch/post/playing-around-with-websockets/) for more information!

<p align="center">
    <img src="https://github.com/akleemans/websocket-example/blob/master/websocket.gif" alt="websocket-example">
</p>

## Frontend

Install `http-server` locally:

    npm install -g http-server
    
The frontend can be served with:

    cd webapp
    http-server
    
Open Browser:

    http://127.0.0.1:8080/

## Backend

Install `pip`:

    sudo apt-get install python-pip 

Install libraries:

    sudo pip install websocket_server

Run:

    python server.py
