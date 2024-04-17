import asyncio
import websockets

class WebSocketClient:
    def __init__(self, symbol):
        self.symbol = symbol
        self.websocket = None
        self.is_connected = False

    async def connect(self):
        uri = f"wss://stream.binance.com:9443/ws/{self.symbol}@trade"
        self.websocket = await websockets.connect(uri)
        self.is_connected = True

    async def listen(self):
        async for message in self.websocket:
            print(f"Received message: {message}")


