import unittest
import rockPaperScissors


class TestRockPaperScissors(unittest.TestCase):
    def test_win(self):
        win = rockPaperScissors.is_win('p', 'r')
        self.assertEqual(win, True)

    def test_lose(self):
        win = rockPaperScissors.is_win('p', 'r')
        self.assertNotEqual(win, False)

    def test_tie(self):
        tie = rockPaperScissors.is_win('p', 'p')
        self.assertNotEqual(tie, False)


if __name__ == '__main__':
    unittest.main()
