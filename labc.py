import asyncio
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol

class EchoClientProtocol(asyncio.Protocol):

    def __init__(self):
        self.transport=None
    def connection_made(self,transport):
        print("Echo Client Connected to Server")
        self.transport=transport
        
        self.deserializer=PacketType.Deserializer()
    def data_received(self,data):
        self._deserializer.update(data)
        print (data)
        
        self.transport.write(data)
        
        for pkt in self.deserializer.nextPackets():
            print (pkt.id)
    def connection_lost(self,exc):
        print("Echo Client Connection lost because {}".format(exc))
        
        self.transport=None

loop1=asyncio.get_event_loop()
loop1.create_connection(lambda:EchoClientProtocol(),host="127.0.0.1",port=8009)
#loop1.run_until_complete()
#loop1.run_forever()
loop1.close()

class EchoServerProtocol(asyncio.Protocol):

    def __init__(self):
        self.transport=None
    def connection_made(self,transport):
        print("Echo Server Connected to Client")
        self.transport=transport
        self.deserializer=PacketType.Deserializer()
    def data_received(self,data):
        self._deserializer.update(data)
        print (data)
        self.transport.write(data)
        for pkt in self.deserializer.nextPackets():
            print (pkt.id)
    def connection_lost(self,exc):
        print("Echo Server Connection lost because {}".format(exc))
        self.transport=None

loop2=asyncio.get_event_loop()
loop2.create_server(lambda:EchoServerProtocol(),port=8009)
#loop2.run_until_complete()
#loop2.run_forever()
loop2.close()

def basicUnitTest():
    asyncio.set_event_loop(TestloopEx())
    client=EchoClientProtocol()
    server=EchoserverProtocol()
    transportToServer=MockTransportToProtocol(server)
    transportToClient=MockTransportToProtocol(client)

    server.make_connection(transportToClient)
    client.make_connection(transportToServer)
    
def main():
    basicUnitTest()
