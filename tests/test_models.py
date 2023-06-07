"""
This file contains the tests for the various data structures
contained in `urban-api/uapi/models.py`.
"""

import unittest

from uapi import User


class TestUserModel(unittest.TestCase):
    """
    - User has `name`
    - `name` is instance of `str`
    - User has email address
    """

    def __init__(self, method_name) -> None:
        super().__init__(method_name)

    def setUp(self) -> None:
        """
        Create instance of `uapi.User`.
        """
        self.user = User(name="John Doe", posts=2, email="doe@example.com")
        return super().setUp()

    def test_name_type(self):
        """
        name is an instance of `str`
        """
        self.assertIsInstance(self.user.name, str)

    def test_email_exists(self):
        """
        user has an email address
        """
        self.assertTrue(self.user.__getattribute__("email"))

    def test_email_type(self):
        """
        email is an instance of `str` or `None`
        """
        self.assertIsInstance(self.user.email, str | None)

    def test_posts_abs(self):
        """
        posts is an absolute value
        """
        self.assertTrue(self.user.posts >= 0)

    def test_posts_type(self):
        """
        posts is an integer
        """
        self.assertIsInstance(self.user.posts, int)


if __name__ == "__main__":
    unittest.main()
