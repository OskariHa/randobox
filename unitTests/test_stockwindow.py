import unittest
from stockwindow import StockWindow


class TestStockWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")

    def setUp(self):
        print("setup")
        self.file = [[1,6],[2,7], [3,2],[4,6],[5,4]]
        #

    def tearDown(self):
        print("teardown")

    def test_get_data(self):
        self.assertEqual(StockWindow.get_data, self.file)



if __name__ == "__main__":
    unittest.main()
