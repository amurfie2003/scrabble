letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
points = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
    4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
]

# Player data
player_to_words = {
    "player1": ["Blue", "Tennis", "Exit"],
    "wordNeard": ["Earth", "Eyes", "Machine"],
    "lexiCon": ["Eraser", "Belly", "Husky"],
    "profReader": ["zap", "comma", "perion"]
}

# Stores the score for each player
player_to_points = {}


letters_points_zipped = zip(letters, points)
letter_to_points = {key: value for key, value in letters_points_zipped}

# Add blank space key value pair to the dictionary
letter_to_points[" "] = 0

# Create function score_word that takes in a word and returns its point value.


def score_word(word):
    score = 0
    word_to_upper = word.upper()

    for c in word_to_upper:
        score += letter_to_points[c]
    return score


# Calculate score.
def update_point_totals():
    for player in player_to_words:
        player_points = 0
        words = player_to_words[player]

        for w in words:
            player_points += score_word(w)
        player_to_points[player] = player_points


# Add a player and word to the game
def play_word(player_name, word):
    if player_name in player_to_words:
        words_played_list = player_to_words[player_name]
        words_played_list.append(word)
    else:
        player_to_words.update({player_name: [word]})


# Test the play_word function
print(player_to_words)
print()
play_word("Murphy", "ZEBRA")
print("After adding player and word")
print(player_to_words)


# Display updatted playes standngs
update_point_totals()
print()
print(player_to_points)
