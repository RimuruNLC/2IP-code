import asyncio
import websockets
async def send(websocket, name, name_two):
    loop = asyncio.get_event_loop()
    while True:
        text = await loop.run_in_executor(None, input, "> ")
        await websocket.send(text+"_"+name+"_" + name_two)
async def receive(websocket):
    while True:
        a = await websocket.recv()
        print(a)


async def main():
    name = str(input("your name? \n>"))
    name_two = str(input("another name? \n>"))
    async with websockets.connect("ws://localhost:8765") as websocket:
        asyncio.create_task(send(websocket,name,name_two))
        asyncio.create_task(receive(websocket))
        await asyncio.sleep(3600)
asyncio.run(main())
