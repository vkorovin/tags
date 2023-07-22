import pytest
import asyncio
from interruptingcow import timeout
import sys
from  tags.game import is_game_finished,handle_user_input,shuffle_field,perform_move,main, print_field

this = sys.modules[__name__]

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


def test_handle_user_input(mocker):
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
    """
    Проверяем правильность обработки пограничных значений ходов и возможность делать правильные ходы
    """

    assert perform_move(FieldSetOnBorder[0], 'w') == None
    assert perform_move(FieldSetOnBorder[1], 's') == None
    assert perform_move(FieldSetOnBorder[2], 'a') == None
    assert perform_move(FieldSetOnBorder[3], 'd') == None

    assert perform_move(FieldSetOnBorder[0], 's') != None
    assert perform_move(FieldSetOnBorder[1], 'd') != None
    assert perform_move(FieldSetOnBorder[2], 'w') != None
    assert perform_move(FieldSetOnBorder[3], 'a') != None

def test_print_field(capfd,mocker, FieldNotFinishGame):
    """
    Проверк печати
    """

    print_field(FieldNotFinishGame)
    out, error = capfd.readouterr()
    assert ' 15  2  3  4 \n\n 5  6  7  8 \n\n 9  10  11  12 \n\n 13  14  1  x \n\n' in out

def test_main_quit(capfd,mocker):
    """
    Проверяем возможность выхода из игры
    """

    mocker.patch('tags.game.handle_user_input', return_value='q')
    main()
    out,error = capfd.readouterr()
    assert '\nBye bye!' in out


def test_main_invalid_move(capfd, mocker,FieldNotFinishGame):
    """
    Проверка того, что правильно обрабатываются неправильны ходы
    способ обработки бескончного while True при помощи asyncio
    """
    mocker.patch('tags.game.handle_user_input', return_value = 'd')
    mocker.patch('tags.game.shuffle_field', return_value=FieldNotFinishGame)
    try:
        with timeout(1, exception=asyncio.CancelledError):
            main().run_once()
    except asyncio.CancelledError:
        out, error = capfd.readouterr()
        assert 'Invalid move!' in out


this.__ONCE__ = True
def my_always_true():
    value = this.__ONCE__
    this.__ONCE__ = False
    return value

def test_main_win(capfd,mocker, FieldFinishGame):
    """
    Проверк того, что можно выиграть  более простой споб прерывания
    игрового цикла, но нужно менять способ получения True в исходном коде
    """

    mocker.patch('tags.game.handle_user_input', return_value='d')
    mocker.patch('tags.game.shuffle_field', return_value=FieldFinishGame)
    mocker.patch('tags.game.always_true', my_always_true)
    main()
    out, error = capfd.readouterr()
    assert '\nYou win ' in out


