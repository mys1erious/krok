import asyncio


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport) -> None:
        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}')
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        message = data.decode()
        print(f'Data received: {message}')

        self.transport.write((f'Echoed back: {message}').encode())

        print(f'Close the client socket')
        self.transport.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
    server = loop.run_until_complete(coro)

    # Server requests until Ctrl+C is pressed
    print(f'Serving on {server.sockets[0].getsockname()}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
