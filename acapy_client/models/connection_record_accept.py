from enum import Enum


class ConnectionRecordAccept(str, Enum):
    MANUAL = "manual"
    AUTO = "auto"

    def __str__(self) -> str:
        return str(self.value)
