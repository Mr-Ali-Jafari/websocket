import asyncio
import websockets

connected_users = set()

async def handle_connection(websocket):
    connected_users.add(websocket)
    try:
        async for message in websocket:
            for user in connected_users:
                if user != websocket:  
                    await user.send(message)
    finally:
        connected_users.remove(websocket)

        
async def start_server():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future() 

asyncio.run(start_server())