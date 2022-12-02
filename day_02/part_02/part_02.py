# define encrypted strategy guide as dicitonaries
round_ends_dict = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
opponent_moves_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}

# define scoring system
shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcome_score = {'Lost': 0, 'Draw': 3, 'Won': 6}

# load input file into list for iterating through encrypted strategy guide
def load_guide(strategy_guide: list):
    open_file = open('input.txt')
    for line in open_file:
        strategy_guide.append(line.strip())
    open_file.close()

# load opponent moves and round ends into lists
def load_moves(opponent_moves: list, round_ends: list, strategy_guide: list):
    # moves are separated by space, so split at the space, append the first
    # part to the opponent moves list, and the second part to the round ends
    for line in strategy_guide:
        opponent_moves.append(line.split(' ')[0])
        round_ends.append(line.split(' ')[1])

# accepts opponent's moves and round ends as strings and returns score
def determine_outcome(opponent_move: str, round_ends: str):
    # unencrypt each move
    opponent_move = opponent_moves_dict[opponent_move]
    round_ends = round_ends_dict[round_ends]

    # draw condition
    if round_ends == 'Draw':
        return shape_score[opponent_move] + outcome_score['Draw']
    # opponent has rock
    elif opponent_move == 'Rock':
        if round_ends == 'Win':
            return shape_score['Paper'] + outcome_score['Won']
        else:
            return shape_score['Scissors'] + outcome_score['Lost']
    # opponent has paper
    elif opponent_move == 'Paper':
        if round_ends == 'Lose':
            return shape_score['Rock'] + outcome_score['Lost']
        else:
            return shape_score['Scissors'] + outcome_score['Won']
    # opponent has scissors
    else:
        if round_ends == 'Win':
            return shape_score['Rock'] + outcome_score['Won']
        else:
            return shape_score['Paper'] + outcome_score['Lost']

def main():
    strategy_guide = []
    round_ends = []
    opponent_moves = []

    # sum of the scores in each round
    total_score = 0

    load_guide(strategy_guide)
    load_moves(opponent_moves, round_ends, strategy_guide)

    # every line in the guide is a round, so determine the outcome of each
    # round, and add to the total score
    for num in range(len(strategy_guide)):
        total_score += determine_outcome(opponent_moves[num], round_ends[num])
    
    print(total_score)

main()