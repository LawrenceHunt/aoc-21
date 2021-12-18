import os


class ScoreCardNumber:

    def __init__(self, number):
        self.is_checked = False
        self.number = number

    def check_number(self, number):
        if self.number == number:
            self.is_checked = True


class ScoreCard:

    def __init__(self, rows, score_card_id=0):
        if len(rows) != 5:
            raise Exception("not a valid score-card!")
        self.id = score_card_id
        self.rows = [[ScoreCardNumber(number) for number in row] for row in rows]
        self.winning_column = None
        self.winning_row = None

    def get_rows(self):
        return self.rows
    
    def get_columns(self):
        return list(zip(self.rows[0], *self.rows[1:]))

    def check_number(self, number):
        for row in self.rows:
            for score_card_number in row:
                score_card_number.check_number(number)

    def check_has_won_horizontal(self):
        for row in self.rows:
            checked_for_row = filter(lambda score_card_number: score_card_number.is_checked, row)
            if len(list(checked_for_row)) == 5:
                self.winning_row = [score_card_number.number for score_card_number in row]

    def check_has_won_vertical(self):
        columns = self.get_columns()
        for column in columns:
            checked_for_column = filter(lambda score_card_number: score_card_number.is_checked, column)
            if len(list(checked_for_column)) == 5:
                self.winning_column = [score_card_number.number for score_card_number in column]

    def get_sum_unchecked_numbers(self):
        sum = 0
        for row in self.rows:
            for num in row:
                if num.is_checked == False:
                    sum += num.number
        return sum

    def print_row(self, row_index):
        return ' '.join([str(score_card_number.number) for score_card_number in self.rows[row_index]])
    
    def print_column(self, column_index):
        columns = self.get_columns()
        return ' '.join([str(score_card_number.number) for score_card_number in columns[column_index]])

    def has_won(self):
        return bool(self.winning_column or self.winning_row)

class Bingo:

    def __init__(self, input_file="test_input.txt"):
        input_path = os.path.join(os.path.dirname(__file__), input_file)
        file = open(input_path, 'r')
        input = file.readlines()
        trimmed_lines = [input_line.rstrip() for input_line in input]
        
        self.game_input = self.extract_game_input(trimmed_lines)
        self.score_cards = self.extract_score_cards(trimmed_lines[1:])
        self.last_called_number = None
        self.winning_answer = None
        self.remaining_score_cards = self.get_remaining_score_cards()
        
        file.close()

    def extract_game_input(self, trimmed_lines):
        return [int(num) for num in trimmed_lines[0].split(',')]
    
    def extract_score_cards(self, trimmed_lines):
        score_cards = []
        current_card_rows = []

        for line in trimmed_lines:
            if line == '':
                continue
            else:
                row = []
                for num_string in line.rstrip().split(' '):
                    stripped_num_string = num_string.rstrip()
                    if len(stripped_num_string) > 0:
                        row.append(int(stripped_num_string))

                score_card_id = len(score_cards)
                if len(current_card_rows) == 5:
                    score_cards.append(ScoreCard(current_card_rows, score_card_id))
                    current_card_rows = [row]
                    continue
                else:
                    current_card_rows.append(row)
                    if len(current_card_rows) == 5:
                        score_cards.append(ScoreCard(current_card_rows, score_card_id))
                        current_card_rows = []

        return score_cards

    def check_number(self, number):
        self.last_called_number = number

        for score_card_index, score_card in enumerate(self.score_cards):
            score_card.check_number(number)
            score_card.check_has_won_horizontal()
            score_card.check_has_won_vertical()
            
            if score_card.has_won():
                self.winning_answer = self.last_called_number * score_card.get_sum_unchecked_numbers()
            if score_card.winning_row:
                print(f"score card {score_card_index} has won on number {number} with row {' '.join([str(num) for num in score_card.winning_row])}! remaining score_card_ids: {' '.join([str(score_card.id) for score_card in self.get_remaining_score_cards()])}")
            if score_card.winning_column:
                print(f"score card {score_card_index} has won on number {number} with column {' '.join([str(num) for num in score_card.winning_column])}! remaining score_card_ids: {' '.join([str(score_card.id) for score_card in self.get_remaining_score_cards()])}")

                

    def first_to_win(self):
        for input_num in self.game_input:
            self.check_number(input_num)
            if self.winning_answer != None:
                return self.winning_answer

    def get_remaining_score_cards(self):
        return list(filter(lambda score_card: score_card.has_won() == False, self.score_cards))

    def last_to_win(self):
        for input_num in self.game_input:
            self.remaining_score_cards = self.get_remaining_score_cards()
            self.check_number(input_num)
            new_remaining_score_cards = self.get_remaining_score_cards()

            if len(self.remaining_score_cards) == 1 and len(new_remaining_score_cards) == 0:
                last_remaining_score_card = self.remaining_score_cards[0]
                print('last', last_remaining_score_card.id)
                print('unchecked nums', last_remaining_score_card.get_sum_unchecked_numbers())
                print('last called', self.last_called_number)
                return last_remaining_score_card.get_sum_unchecked_numbers() * self.last_called_number

