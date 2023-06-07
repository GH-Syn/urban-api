import dataclasses


@dataclasses.dataclass
class User:
    name: str
    posts: int
    email: str
