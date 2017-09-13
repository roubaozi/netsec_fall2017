from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING,UINT32,BOOL
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from Packet import RequestPasswordReset,EmailAnswer,SecurePasswordAns,EmailAsk,SecurePasswordQuest,Result
import asyncio
import playground

class EchoServerProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		print ("Echo Server Connected to Client")
		self.transport=transport
		self.status=0
		self._deserializer=PacketType.Deserializer()
	def data_received(self,data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			print (pkt)
			if isinstance(pkt,RequestPasswordReset):
				packet2=EmailAsk()
				packet2.id=pkt.id
				packet2.emailask="What is your email address?"
				self.status+=1
				self.transport.write(packet2.__serialize__())
			elif isinstance(pkt,EmailAnswer):
				packet4=SecurePasswordQuest()
				packet4.id=pkt.id
				if pkt.emailans=="xyrao@outlook.com":
					packet4.check=True
					packet4.secpwdques="Where is your hometown?"
				else:
					packet4.check=False
					packet4.secpwdques="You email address not exists"
				self.status+=1
				self.transport.write(packet4.__serialize__())
			elif isinstance(pkt,SecurePasswordAns):
				packet6=Result()
				packet6.id=pkt.id
				if pkt.secpwdans=="China":
					packet6.result=True
				else:
					packet6.result=False
				self.status+=1
				self.transport.write(packet6.__serialize__())
			else:
				print ("Wrong!!!")
	def connection_lost(self,exc):
		print ("Echo Server Connection Lost because {}".format(exc))
		self.transport=None
loop=asyncio.get_event_loop()
s=loop.create_server(lambda:EchoServerProtocol(),port=8006)
#s=playground.getConnector().create_playground_server(lambda:EchoServerProtocol(),8080)
loop.run_until_complete(s)
loop.run_forever()
loop.close()
