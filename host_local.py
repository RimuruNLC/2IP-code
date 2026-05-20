import asyncio
import websockets
dict_name = {}
async def echo(websocket):
    async for message in websocket:
        list1 = str(message).split("_")
        dict_name[list1[1]] = websocket
        try:
            await dict_name[list1[2]].send(list1[0])
        except:
            pass

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    await server.wait_closed()
asyncio.run(main())
