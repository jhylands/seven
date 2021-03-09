from thinking import Thought, NonThought, Thinker
from all_thought_generator import set_of_thoughts
from copy import deepcopy as copy
import pytest

def test_thinkmaker():
    # I think we'll run into eq issues with this test
    assert Thinker.thinkmaker() == Thinker.think_type(NonThought(), NonThought(), NonThought(), NonThought(), NonThought(), NonThought(), NonThought())


@pytest.mark.parametrize("thinker", set_of_thoughts())
def test_get_thought(thinker):
    for i in range(1, 7):
        assert thinker[i] is not None
    
@pytest.mark.parametrize("thinker", set_of_thoughts())
@pytest.mark.skip("pass")
def test_rm_thought(thinker):
    for i in range(1, 7):
        thinker_ = copy(thinker)
        thinker_ = thinker.rm(i)
        assert thinker_[i] == NonThought()
