import unittest

from Bingo import Bingo, ScoreCard, ScoreCardNumber


class TestScoreCardNumber(unittest.TestCase):

    def test_init(self):
        score_card_number = ScoreCardNumber(5)
        self.assertEqual(score_card_number.number, 5)
        self.assertEqual(score_card_number.is_checked, False)

    def test_check_number(self):
        score_card_number = ScoreCardNumber(5)
        score_card_number.check_number(3)
        self.assertEqual(score_card_number.is_checked, False)
        score_card_number.check_number(5)
        self.assertEqual(score_card_number.is_checked, True)


class TestScoreCard(unittest.TestCase):

    def test_init_rows(self):
        test_rows = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        score_card = ScoreCard(test_rows)

        for row_index, row in enumerate(test_rows):
            for num_index, num in enumerate(row):
                score_card_number = score_card.rows[row_index][num_index]
                self.assertEqual(
                    score_card_number.number,
                    num, 
                    f"loads score cards successfully for line {row_index} num {num_index}: {num}"
                )
                self.assertEqual(score_card_number.is_checked, False)

    def test_print_column(self):
        test_rows = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        score_card = ScoreCard(test_rows)
        self.assertEqual(score_card.print_column(0), '22 8 21 6 1')
        self.assertEqual(score_card.print_column(1), '13 2 9 10 12')
        self.assertEqual(score_card.print_column(2), '17 23 14 3 20')
        self.assertEqual(score_card.print_column(3), '11 4 16 18 15')
        self.assertEqual(score_card.print_column(4), '0 24 7 5 19')
        
    def test_check_has_won_vertical(self):
        test_rows = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        score_card = ScoreCard(test_rows)
        score_card.check_number(22)
        score_card.check_number(8)
        score_card.check_number(21)
        score_card.check_number(6)
        score_card.check_number(1)
        score_card.check_has_won_vertical()

        self.assertEqual(score_card.winning_column, [22, 8, 21, 6, 1])

    def test_get_sum_unchecked(self):
        test_rows = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        score_card = ScoreCard(test_rows)
        score_card.check_number(0)
        score_card.check_number(24)
        score_card.check_number(7)
        score_card.check_number(5)
        score_card.check_number(19)
        self.assertEqual(score_card.get_sum_unchecked_numbers(), sum(
            [
            22, 13, 17, 11,
            8, 2, 23, 4,
            21, 9, 14, 16,
            6, 10, 3, 18,
            1, 12, 20, 15
        ]
        ))


class TestBingo(unittest.TestCase):

    def test_load_game_input(self):
        bingo = Bingo("test_input.txt")
        expected_game_input = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        self.assertEqual(bingo.game_input, expected_game_input)

    def test_load_score_cards(self):
        bingo = Bingo("test_input.txt")
        self.assertEqual(len(bingo.score_cards), 3)
        expected_score_card_1 = [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ]
        for row_index, row in enumerate(expected_score_card_1):
            for num_index, num in enumerate(row):
                score_card_number = bingo.score_cards[0].rows[row_index][num_index]
                self.assertEqual(
                    score_card_number.number,
                    num, 
                    f"loads score cards successfully for line {row_index} num {num_index}: {num}"
                )

    def test_check_number(self):
        bingo = Bingo("test_input.txt")
        bingo.check_number(22)

        self.assertEqual(bingo.score_cards[0].rows[0][0].is_checked, True)
        self.assertEqual(bingo.score_cards[1].rows[0][4].is_checked, True)
        self.assertEqual(bingo.score_cards[2].rows[3][0].is_checked, True)
        
    def test_check_won_horizontal(self):
        bingo = Bingo("test_input.txt")
        bingo.check_number(22)
        bingo.check_number(13) 
        bingo.check_number(17) 
        bingo.check_number(11) 
        bingo.check_number(0) 

        self.assertEqual(bingo.score_cards[0].winning_row, [22, 13, 17, 11, 0])

    def test_check_won_vertical(self):
        bingo = Bingo("test_input.txt")
        bingo.check_number(22)
        bingo.check_number(8)
        bingo.check_number(21)
        bingo.check_number(6)
        bingo.check_number(1)

        self.assertEqual(bingo.score_cards[0].winning_column, [22, 8, 21, 6, 1])

    def test_first_to_win(self):
        bingo = Bingo("test_input.txt")
        result = bingo.first_to_win()
        expected_result = 4512
        self.assertEqual(result, expected_result)
        
    def test_first_to_win_real(self):
        bingo = Bingo("input.txt")
        result = bingo.first_to_win()
        expected_result = 34506
        self.assertEqual(result, expected_result)
    
    def test_last_to_win(self):
        bingo = Bingo("test_input.txt")
        result = bingo.last_to_win()
        expected_result = 1924
        self.assertEqual(result, expected_result)

    def test_last_to_win_real(self):
        bingo = Bingo("input.txt")
        result = bingo.last_to_win()
        expected_result = 0
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()