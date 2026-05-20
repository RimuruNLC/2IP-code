import asyncio
import websockets
async def send(websocket, name):
    loop = asyncio.get_event_loop()
    while True:
        text = await loop.run_in_executor(None, input, "> ")
        await websocket.send(text+"_"+name)
async def receive(websocket):
    while True:
        a = await websocket.recv()
        print(a)


async def main():
    name = str(input("your name? \n>"))
    async with websockets.connect("ws://26.17.13.154:8765") as websocket:
        asyncio.create_task(send(websocket,name))
        asyncio.create_task(receive(websocket))
        await asyncio.sleep(3600)
asyncio.run(main())
