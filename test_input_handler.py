import pytest
from mock import MagicMock
from input_handler import InputHandler
from thinking import ThoughtPosition


"""
"\d>\d", moving an entity from one place to another
"\d=\d", considering the comparison between two nodes
"=", considering the left right comparison
"c\d", remove the enity from position
# One of the issues here is the type of inferencec
# This, like everything else eventually, will be infered but it'll need to be specific here
"\d", focus on the element, if it doesnt exist try to infer it
"""


@pytest.mark.parametrize("command, arg1, arg2", [
# mv examples
("1>2", 1, 2),
("2>1", 2, 1),
("mv 1 2", 1, 2),
("mv source source_comparison", 1, 2),
("source > source_comparison", 1, 2),
])
def test_input_handler_mv(command, arg1, arg2):
    arg1 = ThoughtPosition(arg1)
    arg2 = ThoughtPosition(arg2)
    mock_thinker = MagicMock()
    handled_input = InputHandler(command)
    handled_input.parse()(mock_thinker)
    mock_thinker.mv.assert_called_with(arg1, arg2)
      
@pytest.mark.parametrize("command, arg", [
("rm 1", 1),
])
def test_input_handler_rm(command, arg):
    arg = ThoughtPosition(arg)
    mock_thinker = MagicMock()
    
    handled_input = InputHandler(command)
    handled_input.parse()(mock_thinker)
    mock_thinker.rm.assert_called_with(arg)
