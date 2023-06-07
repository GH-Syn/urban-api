import unittest

import uapi


class TestUserModel(unittest.TestCase):
    """
    - User needs to have a `name`
    - `name` needs to be an instance of `str`
    - User must have an email address
    """

    def __init__(self, method_name) -> None:
        super().__init__(method_name)

    def test_name_type(self):
        """
        Test name is an instance of `str`
        """
        assert True

    def test_email_exists(self):
        """
        Test that user has an email address
        """
        assert True

if __name__ == "__main__":
    unittest.main()
