import dataclasses


@dataclasses.dataclass
class User:
    name: str
    posts: int
    email: str | None = dataclasses.field(kw_only=True, init=True, default=None)
