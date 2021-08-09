from enum import Enum


class ConnectionRecordInitiator(str, Enum):
    SELF = "self"
    EXTERNAL = "external"
    MULTIUSE = "multiuse"

    def __str__(self) -> str:
        return str(self.value)
