import unittest

from uapi import User


class TestUserModel(unittest.TestCase):
    """
    - User needs to have a `name`
    - `name` needs to be an instance of `str`
    - User must have an email address
    """

    def __init__(self, method_name) -> None:
        super().__init__(method_name)

    def setUp(self) -> None:
        """
        Create an instance of `uapi.User`.
        """
        self.user = User(name="John Doe", posts=2, email="johndoe@example.com")
        return super().setUp()

    def test_name_type(self):
        """
        Test name is an instance of `str`
        """
        self.assertIsInstance(self.user.name, str)

    def test_email_exists(self):
        """
        Test that user has an email address
        """
        self.assertTrue(self.user.__getattribute__('email'))

    def test_email_type(self):
        """
        Test email is an instance of `str`
        """
        self.assertIsInstance(self.user.email, str)


if __name__ == "__main__":
    unittest.main()
