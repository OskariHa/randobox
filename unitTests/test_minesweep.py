import unittest
from minesweep import MineSweep


class TestMineSweepGrid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("setup class")
        d = 1

    @classmethod
    def tearDownClass(cls):
        # print("teardown class")
        m = 1

    def setUp(self):
        # print("setup")
        self.file = [[1, 6], [2, 7], [3, 2], [4, 6], [5, 4]]

    def tearDown(self):
        # print("teardown")
        t = 1

    def test_grid_10(self):
        target_grid_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.grid_size = 10

        self.assertEqual(MineSweep.grid(self), target_grid_list)

    def test_grid_20(self):
        target_grid_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.grid_size = 20
        self.assertEqual(MineSweep.grid(self), target_grid_list)


class TestMineSweepCreateBombs(unittest.TestCase):

    def setUp(self):
        self.grid_size = 10

    def test_grid_10(self):
        self.num_of_bombs = 10

        self.assertEqual(len(MineSweep.create_bombs(self)), 10)

    def test_grid_20(self):
        self.num_of_bombs = 20
        print(self.grid_size)
        self.assertEqual(len(MineSweep.create_bombs(self)), 20)


class TestMineSweepAddBombs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.playing_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def setUp(self):
        s = 1

    def test_add_bombs(self):
        self.bomb_positions = [1, 12, 43, 23, 67, 54, 34, 87, 98, 10]

        MineSweep.add_bombs(self)

        self.assertEqual(self.playing_grid[0][1], 1)
        self.assertEqual(self.playing_grid[1][2], 1)
        self.assertEqual(self.playing_grid[4][3], 1)
        self.assertEqual(self.playing_grid[2][3], 1)
        self.assertEqual(self.playing_grid[6][7], 1)
        self.assertEqual(self.playing_grid[5][4], 1)
        self.assertEqual(self.playing_grid[3][4], 1)
        self.assertEqual(self.playing_grid[8][7], 1)
        self.assertEqual(self.playing_grid[9][8], 1)
        self.assertEqual(self.playing_grid[1][0], 1)

    def test_add_bombs_2(self):
        self.bomb_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        MineSweep.add_bombs(self)

        self.assertEqual(self.playing_grid[0][1], 1)
        self.assertEqual(self.playing_grid[0][2], 1)
        self.assertEqual(self.playing_grid[0][3], 1)
        self.assertEqual(self.playing_grid[0][4], 1)
        self.assertEqual(self.playing_grid[0][5], 1)
        self.assertEqual(self.playing_grid[0][6], 1)
        self.assertEqual(self.playing_grid[0][7], 1)
        self.assertEqual(self.playing_grid[0][8], 1)
        self.assertEqual(self.playing_grid[0][9], 1)


if __name__ == '__main__':
    unittest.main()
