import random
EMPTY_MARK = 'x'
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    seq = list(range(1,16))
    seq.append(EMPTY_MARK)

    #random.shuffle(seq)
    #Simplest, but whorstest way generate game field, cos one half generated results will be unresolvable.

    count = 0
    # Another way generate game field.
    # It generates guaranteed resolvable game, by do 300 valid move. I think, it enough to get good result.
    while count < 300:
        key = random.choice('wsad')
        result =  perform_move(seq, key)
        if  result:
            count += 1

    return(seq)
    #pass


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    #pass
    count = 0
    row = ""
    for item in field:
        row += " {0} ".format(item)
        count += 1
        if count == 4:
            print("{0}\n".format(row))
            row = ""
            count = 0


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    #pass
    if field[-1] == EMPTY_MARK:
        if list(range(1,15))==field[0:14]:
            return True
    return False

def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    current_position = field.index(EMPTY_MARK)
    new_position =  current_position + MOVES[key]
    if ((new_position//4 != current_position//4) and (new_position%4 != current_position%4 ) ) or new_position < 0 or new_position > 15:
        return None
    field[current_position],field[new_position] = field[new_position],field[current_position]
    return field


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """

    move = input()
    if move in "wasdq" and move!='':
        return move
    return None

def always_true():
    return True

def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field = shuffle_field()
    moves_count = 0
    while always_true():
         print_field(field)
         move = handle_user_input()
         while not move:
             print("Invalid move!")
             move = handle_user_input()
         if move == "q":
             print("\nBye bye!")
             break
         newfield = perform_move(field, move)
         if newfield:
             field = newfield
             moves_count += 1
         else:
             print("Invalid move!")           
         if is_game_finished(field):
             print("You win !  {0} moves".format(moves_count))
             break

if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
