import asyncio
import logging


class Client(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop
        self.caps = set()

        #TODO: cleanup logging
        self.log = logging.getLogger()
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.log.addHandler(ch)
        self.log.setLevel(logging.DEBUG)

        self.ibuf = ""
        self.obuf = []
        self.obuf_timer = 2.0


    def connection_made(self, transport):
        self.transport = transport
        self.log.info("Connection created.")
 
    def digest_obuf(self):
        if self.obuf:
            self.write(self.obuf.pop(0))
        loop.call_later(self.obuf_timer, self.digest_obuf)

    def connection_lost(self, exc):
        self.log.error("Lost Connection")

    def data_received(self, data):
        data = data.decode()
	
        self.ibuf += data
        while "\n" in self.ibuf:
            index = self.ibuf.index("\n")
            line = self.ibuf[:index].strip()
            self.ibuf = self.ibuf[index + 1:]

            self.log.debug(line)

    def eof_received(self):
        self.log.info("EOF RECEIVED")


    def register(self, nick, ident, realname, password):
        pass

    def request_capabilities(self):
        self.obuf.append("CAP LS 302")
	  
