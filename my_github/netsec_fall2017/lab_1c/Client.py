from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING,UINT32,BOOL
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from Packet import EmailAsk,SecurePasswordQuest,Result,RequestPasswordReset,EmailAnswer,SecurePasswordAns
import asyncio
import playground

class EchoClientProtocol(asyncio.Protocol):
	def __init__(self):
		#self.loop=loop
		self.transport=None
	def connection_made(self,transport):
		self.transport=transport
		self.status=0
		self._deserializer=PacketType.Deserializer()
		packet1=RequestPasswordReset()
		packet1.id=1
		self.transport.write(packet1.__serialize__())
		#print ("data has been sent")
	def data_received(self,data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			print (pkt)
			if isinstance(pkt,EmailAsk):
				packet3=EmailAnswer()
				packet3.id=pkt.id
				packet3.emailans="xyrao@outlook.com"
				self.status+=1
				self.transport.write(packet3.__serialize__())
			elif isinstance(pkt,SecurePasswordQuest):
				packet5=SecurePasswordAns()
				packet5.id=pkt.id
				packet5.secpwdans="China"
				self.status+=1
				self.transport.write(packet5.__serialize__())
			elif isinstance(pkt,Result):
				print ("You are admitted")
				self.status+=1
			else:
				print ("Wrong!!!")
	def connection_lost(self,exc):
		print ("Echo Client Connection lost because{}".format(exc))		
		self.transport=None

loop=asyncio.get_event_loop()
c=loop.create_connection(lambda:EchoClientProtocol(),host="127.0.0.1",port=8006)
#c=playground.getConnector().create_playground_connection(lambda:EchoClientProtocol(),"20174.1.1.1",8080)
loop.run_until_complete(c)
loop.run_forever()
loop.close()


