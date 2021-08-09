from enum import Enum


class GetConnectionsState(str, Enum):
    REQUEST = "request"
    COMPLETED = "completed"
    INVITATION = "invitation"
    RESPONSE = "response"
    INIT = "init"
    START = "start"
    ERROR = "error"
    ABANDONED = "abandoned"
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
