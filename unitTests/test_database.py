import unittest
from database import create_account


class TestCreateAccount(unittest.TestCase):
    def test_create_account(self):
        # Test empty data values
        result = create_account("osku", "s", "master")
        self.assertFalse(result)
        # self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
