from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BLOCK: _ClassVar[FaultType]
    DEVICE: _ClassVar[FaultType]
    NODE: _ClassVar[FaultType]
BLOCK: FaultType
DEVICE: FaultType
NODE: FaultType

class DevInfo(_message.Message):
    __slots__ = ["dev_info"]
    DEV_INFO_FIELD_NUMBER: _ClassVar[int]
    dev_info: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dev_info: _Optional[_Iterable[str]] = ...) -> None: ...

class VirtDevInfo(_message.Message):
    __slots__ = ["dev_path", "bk_path", "bk_per_dev", "bk_sz"]
    DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    BK_PATH_FIELD_NUMBER: _ClassVar[int]
    BK_PER_DEV_FIELD_NUMBER: _ClassVar[int]
    BK_SZ_FIELD_NUMBER: _ClassVar[int]
    dev_path: str
    bk_path: str
    bk_per_dev: int
    bk_sz: int
    def __init__(self, dev_path: _Optional[str] = ..., bk_path: _Optional[str] = ..., bk_per_dev: _Optional[int] = ..., bk_sz: _Optional[int] = ...) -> None: ...

class VirtDevInfoMultiple(_message.Message):
    __slots__ = ["dev_path", "bk_path", "bk_per_dev", "bk_sz"]
    DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    BK_PATH_FIELD_NUMBER: _ClassVar[int]
    BK_PER_DEV_FIELD_NUMBER: _ClassVar[int]
    BK_SZ_FIELD_NUMBER: _ClassVar[int]
    dev_path: _containers.RepeatedScalarFieldContainer[str]
    bk_path: str
    bk_per_dev: int
    bk_sz: int
    def __init__(self, dev_path: _Optional[_Iterable[str]] = ..., bk_path: _Optional[str] = ..., bk_per_dev: _Optional[int] = ..., bk_sz: _Optional[int] = ...) -> None: ...

class Stat(_message.Message):
    __slots__ = ["stat"]
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: int
    def __init__(self, stat: _Optional[int] = ...) -> None: ...

class Placeholder(_message.Message):
    __slots__ = ["op"]
    OP_FIELD_NUMBER: _ClassVar[int]
    op: int
    def __init__(self, op: _Optional[int] = ...) -> None: ...

class SystemStats(_message.Message):
    __slots__ = ["health"]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    health: int
    def __init__(self, health: _Optional[int] = ...) -> None: ...

class NodeStats(_message.Message):
    __slots__ = ["health"]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    health: int
    def __init__(self, health: _Optional[int] = ...) -> None: ...

class Fault(_message.Message):
    __slots__ = ["fault"]
    FAULT_FIELD_NUMBER: _ClassVar[int]
    fault: FaultType
    def __init__(self, fault: _Optional[_Union[FaultType, str]] = ...) -> None: ...
