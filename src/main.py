import asyncio
from client import Client


def client_connect(server, port):
    client_connection = loop.create_connection(Client, host=server, port=port, ssl=True)
    c_transport, c_protocol = loop.run_until_complete(client_connection)
    return c_protocol

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    client = client_connect("chat.freenode.net",6697)    
    client.register("nickname","ident", "realname", "password")
    loop.run_forever()
    loop.close()
