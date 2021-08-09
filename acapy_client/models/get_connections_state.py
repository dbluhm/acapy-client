from enum import Enum


class GetConnectionsState(str, Enum):
    INIT = "init"
    INVITATION = "invitation"
    REQUEST = "request"
    RESPONSE = "response"
    ACTIVE = "active"
    ERROR = "error"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
