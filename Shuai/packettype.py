from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32,STRING,BUFFER,BOOL

class RequestPicture(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.RequestPicture"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("id",UINT32),
    ]

class Picture(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Picture"
    DEFINITION_VERSION="1.0"
    FIELDS = [
      ("id",UINT32),
      ("picture",BUFFER)
    ]
class Answer(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Answer"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("id",UINT32),
      ("answer",UINT32)
    ]

class Result(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Result"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("id",UINT32),
      ("result",BOOL)
    ]
