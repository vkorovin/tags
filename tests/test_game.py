import pytest

from  tags.game import is_game_finished,handle_user_input,shuffle_field,perform_move

def test_shuffle_field():
    """
    Проверяем уникальность полученного поля d MAX_FILELD_COUNT случаях

    """
    MAX_FILELD_COUNT= 1000
    Fields = list()

    i= 0
    while i < MAX_FILELD_COUNT :
        NewFileld = shuffle_field()
        assert NewFileld not in Fields
        Fields.append(NewFileld)
        i=i+1

def test_handelr_user_input(mocker):
    """
    Проверяем корректность обработки пользовательского ввода
    """
    mocker.patch('builtins.input', return_value='z')
    assert handle_user_input() == None
    mocker.patch('builtins.input', return_value='w')
    assert handle_user_input() == 'w'
    mocker.patch('builtins.input', return_value='a')
    assert handle_user_input() == 'a'
    mocker.patch('builtins.input', return_value='s')
    assert handle_user_input() == 's'
    mocker.patch('builtins.input', return_value='d')
    assert handle_user_input() == 'd'

def test_is_game_finished(FieldFinishGame,FieldNotFinishGame):
    """
    Проверяем возможность закончить игру
    """
    assert is_game_finished(FieldFinishGame) == True
    assert is_game_finished(FieldNotFinishGame) == False

def test_perform_move(FieldSetOnBorder):
    """ Проверяем правильность обработки пограничных значений ходов и пвозможность делать правильные ходы"""
    assert  perform_move(FieldSetOnBorder[0],'w') == None
    assert perform_move(FieldSetOnBorder[1], 's') == None
    assert perform_move(FieldSetOnBorder[2], 'a') == None
    assert perform_move(FieldSetOnBorder[3], 'd') == None

    assert perform_move(FieldSetOnBorder[0], 's') != None
    assert perform_move(FieldSetOnBorder[1], 'd') != None
    assert perform_move(FieldSetOnBorder[2], 'w') != None
    assert perform_move(FieldSetOnBorder[3], 'a') != None
