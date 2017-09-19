from playground.network.packet import PacketType
from playground.network.common import StackingProtocol
from playground.network.common import StackingProtocolFactory
from playground.network.common import StackingTransport
import asyncio
import playground

class PassThrough1(StackingProtocol):
	def __init__(self):
		self.transport=None
	def connection_made(self,transport):
		print ("Connect to the first layer")
		self.transport=transport
		higherTransport=StackingTransport(self.transport)
		self.higherProtocol().connection_made(higherTransport)
	def data_received(self,data):
		self.data=data
		self.higherProtocol().data_received(self.data)
	def connection_lost(self,exc):
		print ("Echo Layer Connection Lost because {}".format(exc))
		self.higherProtocol().connection_lost()

class PassThrough2(StackingProtocol):
	def __init__(self):
		self.transport=None
	def connection_made(self,transport):
		print ("Connect to the second layer")
		self.transport=transport
		higherTransport=StackingTransport(self.transport)
		self.higherProtocol().connection_made(higherTransport)
	def data_received(self,data):
		self.data=data
		self.higherProtocol().data_received(self.data)
	def connection_lost(self,exc):
		print ("Echo Layer Connection Lost because {}".format(exc))
		self.higherProtocol().connection_lost()
