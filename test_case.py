import unittest
from number_guess import check_guess, generate_number
from unittest.mock import patch

class TestGuessingGame(unittest.TestCase):

    def test_check_guess_too_low(self):
        self.assertEqual(check_guess(50, 25), "Too low!")

    def test_check_guess_too_high(self):
        self.assertEqual(check_guess(50, 75), "Too high!")

    def test_check_guess_correct(self):
        self.assertEqual(check_guess(50, 50), "Correct! You win!")

    def test_check_guess_invalid_low(self):
        self.assertEqual(check_guess(50, 0), "Invalid input! Enter a number between 1 and 100.")

    def test_check_guess_invalid_high(self):
        self.assertEqual(check_guess(50, 101), "Invalid input! Enter a number between 1 and 100.")

    @patch('number_guess.random.randint')
    def test_generate_number_range(self, mock_randint):
        mock_randint.return_value = 42
        number = generate_number()
        self.assertEqual(number, 42)

if __name__ == "__main__":
    unittest.main()