import dataclasses


@dataclasses.dataclass
class User:
    name: str
    posts: int
    email: str = dataclasses.field(kw_only=True, init=False)
