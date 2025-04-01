from enum import Enum


class APIRoutes(str, Enum):
    LIST_USERS_GET = "/api/users?page=2"

    def __str__(self) -> str:
        return self.value
