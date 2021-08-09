from enum import Enum


class GetConnectionsInitiator(str, Enum):
    SELF = "self"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
