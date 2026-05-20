import asyncio
import websockets
name = set()
async def echo(websocket):
    async for message in websocket:
        print(1)
        list1 = str(message).split("_")
        name.add(websocket)
        print(name)
        try:
            for i in name:
                await i.send(list1[0])
        except:
            print(2)

async def main():
    server = await websockets.serve(echo, "0.0.0.0", 8765)
    await server.wait_closed()
asyncio.run(main())
