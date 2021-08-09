from enum import Enum


class GetRevocationRegistriesCreatedState(str, Enum):
    INIT = "init"
    GENERATED = "generated"
    PUBLISHED = "published"
    STAGED = "staged"
    ACTIVE = "active"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
