# define encrypted strategy guide as dicitonaries
player_moves_dict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
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

# load opponent and player moves into lists
def load_moves(opponent_moves: list, player_moves: list, strategy_guide: list):
    # moves are separated by space, so split at the space, append the first
    # part to the opponent moves list, and the second part to the player
    for line in strategy_guide:
        opponent_moves.append(line.split(' ')[0])
        player_moves.append(line.split(' ')[1])

# accepts opponent and player's moves as strings and returns total score
def determine_outcome(opponent_move: str, player_move: str):
    # unencrypt each move
    opponent_move = opponent_moves_dict[opponent_move]
    player_move = player_moves_dict[player_move]

    # draw condition
    if opponent_move == player_move:
        return shape_score[player_move] + outcome_score['Draw']
    # opponent has rock
    elif opponent_move == 'Rock':
        if player_move == 'Paper':
            return shape_score['Paper'] + outcome_score['Won']
        else:
            return shape_score['Scissors'] + outcome_score['Lost']
    # opponent has paper
    elif opponent_move == 'Paper':
        if player_move == 'Rock':
            return shape_score['Rock'] + outcome_score['Lost']
        else:
            return shape_score['Scissors'] + outcome_score['Won']
    # opponent has scissors
    else:
        if player_move == 'Rock':
            return shape_score['Rock'] + outcome_score['Won']
        else:
            return shape_score['Paper'] + outcome_score['Lost']

def main():
    strategy_guide = []
    player_moves = []
    opponent_moves = []

    # sum of the scores in each round
    total_score = 0

    load_guide(strategy_guide)
    load_moves(opponent_moves, player_moves, strategy_guide)

    # every line in the guide is a round, so determine the outcome of each
    # round, and add to the total score
    for num in range(len(strategy_guide)):
        total_score += determine_outcome(opponent_moves[num], player_moves[num])
    
    print(total_score)

main()