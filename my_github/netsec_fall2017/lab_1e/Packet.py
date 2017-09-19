from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import STRING,UINT32,BOOL

class RequestPasswordReset(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.RequestPasswordReset"
	DEFINITION_VERSION="1.0"
	
	FIELDS=[
		("id",UINT32)
		]

class EmailAsk(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.EmailAsk"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("emailask",STRING),
		("id",UINT32)
		]

class EmailAnswer(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.EmailAnswer"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("emailans",STRING),
		("id",UINT32)
		]

class SecurePasswordQuest(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.SecurePasswordQuest"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("check",BOOL),		
		("secpwdques",STRING),
		("id",UINT32)
		]
		
class SecurePasswordAns(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.SecurePasswordAns"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("secpwdans",STRING),
		("id",UINT32)
		]

class Result(PacketType):
	DEFINITION_IDENTIFIER="lab1b.rxy.Result"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("result",BOOL),
		("id",UINT32)
		]

