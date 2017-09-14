import asyncio
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from packettype import RequestPicture,Picture,Answer,Result
from client import EchoClientProtocol
from server import EchoServerProtocol
from playground.network.packet import PacketType

def basicUnitTest():
    asyncio.set_event_loop(TestloopEx())
    client=EchoClientProtocol()
    server=EchoserverProtocol()
    transportToServer=MockTransportToProtocol(server)
    transportToClient=MockTransportToProtocol(client)

    server.connection_made(transportToClient)
    client.connection_made(transportToServer)

    packet1=RequestPicture()
    packet1.id=1
    client.transport.write(packet1.__serizalize__())
     
    assert client.status==2
    assert server.status==2
    
def main():
    basicUnitTest()
