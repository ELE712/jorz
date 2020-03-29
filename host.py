#!/usr/bin/env python3

import asyncio
import websockets
import datetime
from logging import getLogger, INFO, StreamHandler

logger = getLogger('websockets')
logger.setLevel(INFO)
logger.addHandler(StreamHandler())

current_sleep = .017

socket_infos = set()


async def handler(websocket, path):
	global socket_infos
	global current_sleep
	wi = create_websocket_info(websocket)
	socket_infos.add(wi)

	try:
		wi.name = await websocket.recv()
	except websockets.ConnectionClosed:
		print("Terminated")

	while True:
		await websocket.send(get_send_data(wi))
		await asyncio.sleep(current_sleep)

	socket_infos.remove(wi)
	print("whatthefuck")

ugly_fo = []
for i in range(100000):
	ugly_fo.append("a")

ugly = "".join(ugly_fo)

def get_send_data(wi):
	global socket_infos
	global ugly
	wi.count += 1
	buff = wi.out_buff
	wi.out_buff.clear()
	wi.out_send = buff

	uglym = ""
	return str(wi.count) + wi.name + ugly #wi.out_send

def handle_in_stream(instream):
	return "FOOEY"
	
def create_websocket_info(websocket):
	return WebsocketInfo(websocket)

# while True:
# 	global socket_infos
	# for socket_info in socket_infos:

class WebsocketInfo:
	def __init__(self, websocket):
		self.name = "<NONE>"
		self.websocket = websocket
		self.channel = 0
		self.count = 1
		self.in_buff = []
		self.out_buff = []
		self.in_send = []
		self.out_send = []


# async def ws_loop():
# 	while True:
# 		await asyncio.sleep(3)
# 		global clients
# 		if clients:
# 			for ws in clients:
# 				now = datetime.datetime.utcnow().isoformat() + "Z"
# 				await ws.send(now)

	#return [ws.send("Hello!") for ws in clients]

start_server = websockets.serve(handler, port=6969)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



# agent = FlashServer()   # a new RTMP server instance
# agent.start()           # start the server
# multitask.run()         # this is needed somewhere in the application to actually start the co-operative multitasking.

# class MyApp(App):         # a new MyApp extends the default App in rtmp module.
# 	def __init__(self):   # constructor just invokes base class constructor
# 		App.__init__(self)
# 	def onConnect(self, client, *args):
# 		result = App.onConnect(self, client, *args)   # invoke base class method first
# 		def invokeAdded(self, client):                # define a method to invoke 'connected("some-arg")' on Flash client
# 			yield client.call('connected', 'some-arg')
# 		multitask.add(invokeAdded(self, client))      # need to invoke later so that connection is established before callback
# 		return result     # return True to accept, or None to postpone calling accept()

# agent.apps = dict({'*': MyApp})
