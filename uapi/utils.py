"""
Copyright 2023 Joshua Rose
--------------------------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
or in the `LICENSE` file at https://github.com/GH-Syn/urban-api/blob/main/LICENSE

Description
-----------
The three 'pillars' of `urban-api/uapi/utils.py`
 1. retrieve info with the `requests` module.
 2. format said info with `bs4` module.
 3. display said info with `rich` module.
"""



def fetch_posts_from_user(name: str, page=0) -> int:
    """Index number of posts from a user.

    If a `page` keyword agument is specified, `fetch_posts_from_user` will
    index the number of posts on that specific page, instead of the total
    number of posts from `name`.

    :param name: Any existant `name` such as "John Doe".
    :param page: The page to index from.
    :raises NameNotExistsError: If the name doesn't exist in the UD.
    :return: The number of posts that `name` has posted.
    """
