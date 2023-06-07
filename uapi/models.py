"""
Copyright 2023 Joshua Rose
--------------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
or in the `LICENSE` file at https://github.com/GH-Syn/urban-api/blob/main/LICENSE

Description
-----------
This file holds models and classes that are needed.
Any basic data structures will be found here.
"""

import dataclasses


@dataclasses.dataclass
class User:
    name: str
    posts: int
    email: str | None = dataclasses.field(kw_only=True, init=True, default=None)
