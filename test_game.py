import unittest
import testing_number_game


class TestGame(unittest.TestCase):
    def test_input(self):
        result = testing_number_game.run_guess(5, 5)  # (answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = testing_number_game.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = testing_number_game.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = testing_number_game.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
