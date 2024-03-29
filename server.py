#!/usr/local/bin/python
# documentation: https://github.com/Pithikos/python-websocket-server
import json
from websocket_server import WebsocketServer

from board import Board


def new_client(client, server):
    print "new client! -> ", client['id']


def client_left(client, server):
    print "client disconnected:", client['id']


def message_received(client, server, message):
    print "client ", client['id'], " sent: ", message
    msg = json.loads(message)
    print "client", client['id'], "sent action", msg['action'], 'data', msg['data']

    if msg['action'] == 'REQUEST_NEW_GAME':
        print 'Handling new game!'
        handleNewGame(client)
    elif msg['action'] == 'REQUEST_MOVE':
        handleMove(client, msg['data']['from'], msg['data']['to'])
    else:
        print 'Error: Unknown action! => ', msg['action']


def handleNewGame(client):
    sendMessage(client, 'NEW_GAME', str(board))


def handleMove(client, start, target):
    board.move(start, target)
    board.remove_duplicates(True)
    sendMessage(client, 'NEW_GAME', str(board))


def sendMessage(client, action, data):
    message = {
        'action': action,
        'data': data
    }
    json_msg = json.dumps(message)
    print 'sending message:', json_msg
    server.send_message(client, json_msg)


# init board
board = Board()

# init websocket
server = WebsocketServer(5678, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
