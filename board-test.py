import unittest

from board import Board


class TestBoard(unittest.TestCase):

    def test_get_coords(self):
        """ testing conversion of position to coordinates """
        board = Board(test=True)
        self.assertEqual(board.get_coords(0), (0, 0))
        self.assertEqual(board.get_coords(1), (1, 0))
        self.assertEqual(board.get_coords(8), (0, 1))
        self.assertEqual(board.get_coords(9), (1, 1))
        self.assertEqual(board.get_coords(63), (7, 7))
        self.assertEqual(board.get_coords(15), (7, 1))
        self.assertEqual(board.get_coords(31), (7, 3))
        self.assertEqual(board.get_coords(35), (3, 4))
        self.assertEqual(board.get_coords(36), (4, 4))

    def test_set_from_string(self):
        """ test setting the board from string """
        s = 'pgbbogoopwppygobyorgrryrbrbbprgbyoggpgrbrgywpwyybopwrrogwppbrrpo'
        expected_board = ['p', 'g', 'b', 'b', 'o', 'g', 'o', 'o']
        board = Board(test=True)
        actual_board = board.set_from_string(s)
        self.assertEqual(actual_board[:8], expected_board[:8])

    def test_get_aligned_gems(self):
        """
        test fetching of gems nearby
        pgbbogoo
        pwppygob
        yorgrryr
        brbbprgb
        yoggpgrb
        rgywpwyy
        bopwrrog
        wppbrrpo
        """
        board = Board(test=True)
        board.set_from_string('pgbbogoopwppygobyorgrryrbrbbprgbyoggpgrbrgywpwyybopwrrogwppbrrpo')
        self.assertEqual(board.get_aligned_gems(0), set(['g', 'p']))
        self.assertEqual(board.get_aligned_gems(9), set(['p', 'g', 'o']))
        self.assertEqual(board.get_aligned_gems(48), set(['r', 'o', 'w']))
        self.assertEqual(board.get_aligned_gems(56), set(['p', 'b']))
        self.assertEqual(board.get_aligned_gems(63), set(['p', 'g']))


if __name__ == '__main__':
    unittest.main()
