from unittest import TestCase
from boggle import Boggle
import unittest


class FlaskTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_invalid_word(self):
        board_object = Boggle(board_size=6)
        self.assertEqual(
            board_object.check_valid_word(board_object.board, "人人人人人人"),
            "not-word",
        )

    def test_check_valid_word(self):
        board_contents = [
            ["T", "E", "S", "T", "S"],
            ["T", "E", "S", "T", "S"],
            ["T", "E", "S", "T", "S"],
            ["T", "E", "S", "T", "S"],
            ["T", "E", "S", "T", "S"],
        ]
        board_object = Boggle(board_size=6, board=board_contents)
        self.assertEqual(
            board_object.check_valid_word(board_object.board, "tests"), "ok"
        )

    def test_check_valid_word_on_end_of_board(self):
        board_contents = [
            ["F", "D", "T", "G", "E", "J"],
            ["I", "Q", "E", "G", "E", "M"],
            ["K", "T", "Z", "A", "Y", "N"],
            ["V", "N", "J", "N", "D", "C"],
            ["J", "Y", "O", "M", "Q", "X"],
            ["J", "W", "J", "C", "P", "I"],
        ]
        board_object = Boggle(board_size=6, board=board_contents)
        self.assertEqual(
            board_object.check_valid_word(board_object.board, "gem"), "ok"
        )


if __name__ == "__main__":
    unittest.main()
