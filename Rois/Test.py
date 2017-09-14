from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING,UINT32,BOOL
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from Packet import RequestPasswordReset,EmailAnswer,SecurePasswordAns,EmailAsk,SecurePasswordQuest,Result
from Client import EchoClientProtocol
from erver import EchoServerProtocol
import asyncio

def basicUnitTest():
	asyncio.set_event_loop(TestLoopEx())
	client=EchoClientProtocol()
	server=EchoServerProtocol()
	transportToServer=MockTransportToProtocol(server)
	transportToClient=MockTransportToProtocol(client)

	server.connection_made(transportToClient)
	client.connection_made(transportToServer)

	assert client.status==3
	assert server.status==3

def __main():
	basicUnitTest()
