import sys
import pytest
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
@pytest.fixture
def FieldFinishGame():
    return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'x']
@pytest.fixture
def FieldNotFinishGame():
    return [15,2,3,4,5,6,7,8,9,10,11,12,13,14,1,'x']
@pytest.fixture
def FieldBeforeFinishGame():
    return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,'x',15]
@pytest.fixture
def FieldSetOnBorder():
    return [
           [15, 2, 'x', 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 3],
           [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'x', 1],
           [15, 2, 3, 4, 'x', 6, 7, 5, 9, 10, 11, 12, 13, 14, 1, 8],
           [15, 2, 3, 4, 5, 6, 7, 'x', 9, 10, 11, 12, 13, 14, 1, 8],
           ]