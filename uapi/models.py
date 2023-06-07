"""
Copyright 2023 Joshua Rose
--------------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
or in the `LICENSE` file at https://github.com/GH-Syn/urban-api/blob/main/LICENSE
"""

import dataclasses


@dataclasses.dataclass(order=False, frozen=True)
class User:
    """
    This is a data class representing a User object.

    It is annotated with type hints and follows the data class pattern.

    :param str name: Username is an alphanumeric value
    :param int posts: Number of definitions created
    :param dict kwargs: Additional keyword arguments
    """

    name: str
    posts: int
    email: str | None = dataclasses.field(kw_only=True, init=True, default=None)
