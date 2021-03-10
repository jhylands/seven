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
def test_set_thought(thinker):
    for i in range(1, 7):
        thought = Thought()
        thinker[i] = thought
        assert thinker[i] == thought
    
@pytest.mark.parametrize("thinker", set_of_thoughts())
def test_rm_thought(thinker):
    for i in range(1, 7):
        thinker_ = copy(thinker)
        thinker_.rm(i)
        assert isinstance(thinker_[i], NonThought)

@pytest.mark.parametrize("thinker", set_of_thoughts())
def test_mk_thought(thinker):
    for i in range(1, 7):
        thinker_ = copy(thinker)
        thinker_.mk(i, "my thought")
        assert thinker_[i].representation == "my thought"

@pytest.mark.parametrize("thinker", set_of_thoughts())
def test_mv_thought(thinker):
    for i in range(1, 7):
        for j in range(1, 7):
            thinker_ = copy(thinker)
            thought = Thought()
            thinker_[i] = thought
            thinker_.mv(i, j)
            assert thinker_[j] == thought
# Not sure what is going on here
#            print(thinker_[i])
#            assert thinker_[i] == thought
#            assert isinstance(thinker_[i], Thought) or thinker_[i] == thought
