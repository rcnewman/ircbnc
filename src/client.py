import asyncio
import logging


class Client(asyncio.Protocol):
    """
    Client connection to IRC
    """

    def connection_made(self, transport):
        self.transport = transport

        #TODO: cleanup logging
        self.log = logging.getLogger()
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.log.addHandler(ch)
        self.log.setLevel(logging.DEBUG)

        self.ibuf = ""
        self.obuf = []

        self.log.info("Connection created.")

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
